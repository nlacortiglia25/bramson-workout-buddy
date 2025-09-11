import cv2
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from mediapipe.framework.formats import landmark_pb2

print("Starting live webcam pose detection")

# Paths
model_path = './models/pose_landmarker_lite.task'
output_path = './webcam_output.mp4'

# Aliases
BaseOptions = mp.tasks.BaseOptions
PoseLandmarker = mp.tasks.vision.PoseLandmarker
PoseLandmarkerOptions = mp.tasks.vision.PoseLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

# Drawing utils
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# Buffer joint data
sequence_length = 30  # number of frames per input
joint_buffer = []     # stores joint keypoints over time


# Create pose landmarker
options = PoseLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    running_mode=VisionRunningMode.VIDEO
)

with PoseLandmarker.create_from_options(options) as landmarker:
    cap = cv2.VideoCapture(0)  # Use webcam
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        exit()

    fps = 30  # approximate webcam FPS
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # VideoWriter for saving annotated video
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    frame_idx = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
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

                # Extract x, y, z for each joint
                joints = np.array([[lm.x, lm.y, lm.z] for lm in result.pose_landmarks[0]])
                joint_buffer.append(joints)

                # Keep buffer size constant
                if len(joint_buffer) > sequence_length:
                    joint_buffer.pop(0)

        # Write annotated frame
        out.write(frame)

        # Optional: show live window (remove if running headless)
        cv2.imshow("Webcam Pose", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        frame_idx += 1

    cap.release()
    out.release()
    cv2.destroyAllWindows()

print(f"Finished webcam processing. Video saved to {output_path}")
