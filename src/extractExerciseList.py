import os
import glob
import os

print(os.getcwd())

root_dir = '..\\..\\exercise_dataset'
sequences_dataset = []
output_file = 'exercise_types.txt'
list_of_exercises = None

with open(output_file, 'w') as f:
    print("opening output stream")
    for subdir, dirs, files in os.walk(root_dir):
        list_of_exercises = str(dirs)
        print(list_of_exercises)
        break
    print("writing to file...")
    f.write(list_of_exercises)
        
 

