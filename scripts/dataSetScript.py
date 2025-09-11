import os
import glob
from videoLandmarker import getLandmarks, saveLandmarks

root_dir = '..\\..\\test_data_set'
sequences_dataset = []

for subdir, dirs, files in os.walk(root_dir):
    video_files = glob.glob(os.path.join(subdir, '*.mp4'))  # Change extension if needed
    for video_path in video_files:
        # Do something with each video
        print(f'Processing: {video_path}')
        sequence_obj = getLandmarks(video_path, subdir.split('\\')[-1])
        sequences_dataset.append(sequence_obj)
        # Example: process_video(video_path

saveLandmarks(sequences_dataset)