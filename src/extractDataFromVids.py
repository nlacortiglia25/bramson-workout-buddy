import os
import glob
from videoLandmarker import getLandmarksVideo, saveLandmarks
from featureExtraction import extract_joint_angles

root_dir = '..\\verified_data'
sequences_dataset = []

for subdir, dirs, files in os.walk(root_dir):
    video_files = glob.glob(os.path.join(subdir, '*.mp4'))
    for video_path in video_files:
        print(f'Processing: {video_path}')
        sequence_obj = getLandmarksVideo(video_path, subdir.split('\\')[-1])
        sequence_obj = extract_joint_angles(sequence_obj)
        sequences_dataset.append(sequence_obj)

saveLandmarks(sequences_dataset)