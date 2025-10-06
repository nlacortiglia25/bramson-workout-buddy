import joblib
import cv2
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from mediapipe.framework.formats import landmark_pb2
from featureExtraction import extract_joint_angles
from motivationGeneration import generate_motivation
from tts import text_to_speech
import threading
import queue

print("Starting...")

# Paths
pose_model_path = './models/pose_landmarker_lite.task'
exercise_model_path = "./models/exercise_classify_model.pkl"
exercise_encoder_path = "./models/exercise_label_encoder.pkl"

# Vars
BaseOptions = mp.tasks.BaseOptions
PoseLandmarker = mp.tasks.vision.PoseLandmarker
PoseLandmarkerOptions = mp.tasks.vision.PoseLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode
tts_queue = queue.Queue()
tts_thread = threading.Thread(target=text_to_speech, args=(tts_queue,), daemon=True)
tts_thread.start()
curr_exercise = None 
prev_exercise = None

# Input Parameters
SPEACH_INTERVAL = 10000#ms


joint_map = [
"nose", "left eye (inner)", "left eye", "left eye (outer)", "right eye (inner)", "right eye", "right eye (outer)",
"left ear", "right ear", "mouth (left)", "mouth (right)", "left shoulder", "right shoulder", "left elbow", "right elbow",
"left wrist", "right wrist", "left pinky", "right pinky", "left index", "right index", "left thumb", "right thumb",
"left hip", "right hip", "left knee", "right knee", "left ankle", "right ankle", "left heel", "right heel",
"left foot index", "right foot index"
]

# Drawing utils
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# Load exercise classification model
print("Importing models...")
model = joblib.load(exercise_model_path)
encoder = joblib.load(exercise_encoder_path)

# Buffer joint data
sequence_length = 120  # number of frames per input
world_pose_buffer = [] # store world poses over time in a sequence

# Create pose landmarker
options = PoseLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=pose_model_path),
    running_mode=VisionRunningMode.VIDEO
)
with PoseLandmarker.create_from_options(options) as landmarker:
    cap = cv2.VideoCapture(0)  # Use webcam
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        exit()

    fps = int(cap.get(cv2.CAP_PROP_FPS))
    if fps == 0: 
        fps = 30 # Default to 30 FPS if reads as 0.0 for now.
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    frame_idx = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB).copy()
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame_rgb)
        timestamp_ms = int((frame_idx / fps) * 1000)

        result = landmarker.detect_for_video(mp_image, timestamp_ms)

        if result.pose_landmarks:
            for landmarks in result.pose_landmarks:
                landmark_proto = landmark_pb2.NormalizedLandmarkList(
                    landmark=[
                        landmark_pb2.NormalizedLandmark(
                            x=lm.x, y=lm.y, z=lm.z, visibility=lm.visibility
                        ) for lm in landmarks
                    ]
                )

                # Draw landmarks on the frame
                mp_drawing.draw_landmarks(
                    frame,
                    landmark_proto,
                    mp.solutions.pose.POSE_CONNECTIONS,
                    landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style()
                )

                # Only index the first pose detected
                if len(result.pose_world_landmarks) == 0:
                    frame_idx += 1
                    continue
                pose = {}
                for index, landmark in enumerate(result.pose_world_landmarks[0]):
                    pose[joint_map[index]] = {
                        'x': landmark.x,
                        'y': landmark.y,
                        'z': landmark.z,
                        'visibility': landmark.visibility,
                        'coordinate': (landmark.x, landmark.y, landmark.z)
                    }
                world_pose_buffer.append(pose)
                # Keep buffer size constant
                if len(world_pose_buffer) > sequence_length:
                    # Extract and predict here
                    sequence_obj = extract_joint_angles(world_pose_buffer, True)
                    
                    seq_numeric = []
                    for obj in sequence_obj:
                        values = [obj[k] for k in sorted(obj.keys())]  # alphabetical order
                        seq_numeric.append(values)

                    seq_array = np.array(seq_numeric)  # shape = (frames, features)
                    
                    features = np.concatenate([
                        seq_array.mean(axis=0),
                        seq_array.std(axis=0),
                        seq_array.min(axis=0),
                        seq_array.max(axis=0)
                    ])

                    # Predict numeric label
                    numeric_pred = model.predict(features.reshape(1, -1))
                    # Convert to human-readable label
                    predicted_label = encoder.inverse_transform(numeric_pred)
                    curr_exercise = predicted_label[0]
                    print(f"Current ts {timestamp_ms}")

                    if curr_exercise != prev_exercise or prev_exercise == None:
                        print(f"New exercise: {curr_exercise} detected...")

                    if timestamp_ms % SPEACH_INTERVAL == 0: # Every 10 seconds
                        print(f"10 seconds passed (timestamp = {timestamp_ms}), now generating message")
                        message = generate_motivation(curr_exercise, "gym_bro")
                        tts_queue.put(message, block=True)

                    prev_exercise = curr_exercise
                    world_pose_buffer.pop(0)

        # Live window
        cv2.imshow("Webcam Pose", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        frame_idx += 1

    cap.release()
    cv2.destroyAllWindows()

print(f"Finished webcam processing.")