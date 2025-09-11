import cv2
import json
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from mediapipe.framework.formats import landmark_pb2

# Save landmarks as a json
def saveLandmarks(sequences_dataset, output_file='landmarks_dataset.json'):
    with open(output_file, 'w') as f:
        json.dump(sequences_dataset, f)
    print(f"Landmarks saved to {output_file}")

# Extract landmarks from a video file, build up a sequence, label it with the exercise type, then return it
def getLandmarks(video_path, exercise_type):
    # Paths
    model_path = './models/pose_landmarker_lite.task'

    # Aliases
    BaseOptions = mp.tasks.BaseOptions
    PoseLandmarker = mp.tasks.vision.PoseLandmarker
    PoseLandmarkerOptions = mp.tasks.vision.PoseLandmarkerOptions
    VisionRunningMode = mp.tasks.vision.RunningMode
    result = None
    sequence = []

    # Drawing utils
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles

    print("Creating pose landmark instance with the video mode")
    options = PoseLandmarkerOptions(
        base_options=BaseOptions(model_asset_path=model_path),
        running_mode=VisionRunningMode.VIDEO
    )

    with PoseLandmarker.create_from_options(options) as landmarker:
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            print("Error: Could not open video.")
            exit()

        # Video properties
        fps = cap.get(cv2.CAP_PROP_FPS)

        frame_idx = 0

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame_rgb)
            timestamp_ms = int((frame_idx / fps) * 1000)

            result = landmarker.detect_for_video(mp_image, timestamp_ms)

            # Only index the first pose detected
            if len(result.pose_world_landmarks) == 0:
                frame_idx += 1
                continue
            
            for landmark in result.pose_world_landmarks[0]:
                sequence.append({
                    'x': landmark.x,
                    'y': landmark.y,
                    'z': landmark.z,
                    'visibility': landmark.visibility,
                })

            frame_idx += 1

        cap.release()
        print(f"Finished processing landmarks for {video_path}")
        return {'exercise_type': exercise_type, 'sequence': sequence}
