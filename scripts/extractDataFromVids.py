import os
import glob
from videoLandmarker import getLandmarks, saveLandmarks
from featureExtraction import extract_joint_angles

root_dir = '..\\test_data_set'
sequences_dataset = []

for subdir, dirs, files in os.walk(root_dir):
    video_files = glob.glob(os.path.join(subdir, '*.mp4'))
    for video_path in video_files:
        print(f'Processing: {video_path}')
        sequence_obj = getLandmarks(video_path, subdir.split('\\')[-1])
        sequence_obj = extract_joint_angles(sequence_obj)
        # print(f"Appending sequence: {sequence_obj} to dataset...")
        sequences_dataset.append(sequence_obj)

# for (index, seq) in enumerate(sequences_dataset):
#     print(f"Sequence {index}: {seq}")

# print(sequences_dataset)
saveLandmarks(sequences_dataset)