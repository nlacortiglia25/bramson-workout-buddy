import math as m


def main():

    # Triangle formula test
    a = 10
    b = 11
    c = 17

    A = find_triangle_angle(a, b, c)
    print(A)
    assert m.floor(A) == 34
    print("Test 1 passed!")
    
    a = 1
    b = 1
    c = 1

    A = find_triangle_angle(a, b, c)
    print(A)
    assert m.floor(A) == 60
    print("Test 2 passed!")

    a = 20
    b = 110
    c = 120

    A = find_triangle_angle(a, b, c)
    print(A)
    assert m.floor(A) == 8
    print("Test 3 passed!")


    

# Given a sequence of body poses, extract the necessary joint angles, then return the joint angles in temporal order
# Input: Dictionary such that {'exercise_type': exercise_type, 'sequence': sequence}
# Output: List of dictionaries such that [{'exercise_type': exercise_type, 'sequence': [frame1_angles, frame2_angles, ...]}]

def extract_joint_angles(pose_sequence):
    
    print("Extracting joint angles from pose sequence...")
    joint_sequence = {'exercise_type': pose_sequence['exercise_type'], 'sequence': []}

    print(f"Length of the input pose sequence: {len(pose_sequence['sequence'])}")

    for pose in pose_sequence['sequence']:
        joint_angles = {}
        # Add shoulder rotation eventually
        # Left Shoulder

        # Add shoulder rotation eventually
        # Right Shoulder
        
        
        # Left Elbow
        print("Calculating left elbow angle...")
        lwrist_to_lelbow = m.dist((pose["left wrist"]['coordinate']), pose["left elbow"]['coordinate'])
        print(f"Distance between left wrist {pose['left wrist']['coordinate']} and left elbow {pose['left elbow']['coordinate']}: {lwrist_to_lelbow}")
        lelbow_to_lshoulder = m.dist(pose["left elbow"]['coordinate'], pose["left shoulder"]['coordinate'])
        print(f"Distance between left elbow {pose['left elbow']['coordinate']} and left shoulder {pose['left shoulder']['coordinate']}: {lelbow_to_lshoulder}")
        lshoulder_to_lwrist = m.dist(pose["left shoulder"]['coordinate'], pose["left wrist"]['coordinate'])
        print(f"Distance between left shoulder {pose['left shoulder']['coordinate']} and left wrist {pose['left wrist']['coordinate']}: {lshoulder_to_lwrist}")
        left_elbow_angle = find_triangle_angle(lshoulder_to_lwrist, lwrist_to_lelbow, lelbow_to_lshoulder)
        print(f"Left elbow angle: {left_elbow_angle} degrees")

        joint_angles['left elbow'] = left_elbow_angle

        # Right Elbow
        rwrist_to_relbow = m.dist(pose["right wrist"]['coordinate'], pose["right elbow"]['coordinate'])
        relbow_to_rshoulder = m.dist(pose["right elbow"]['coordinate'], pose["right shoulder"]['coordinate'])
        rshoulder_to_rwrist = m.dist(pose["right shoulder"]['coordinate'], pose["right wrist"]['coordinate'])
        right_elbow_angle = find_triangle_angle(rshoulder_to_rwrist, rwrist_to_relbow, relbow_to_rshoulder)
        joint_angles['right elbow'] = right_elbow_angle

        # Left Wrist
        lwrist_to_lelbow = m.dist(pose["left wrist"]['coordinate'], pose["left elbow"]['coordinate'])
        lelbow_to_lindex = m.dist(pose["left elbow"]['coordinate'], pose["left index"]['coordinate'])
        lindex_to_lwrist = m.dist(pose["left index"]['coordinate'], pose["left wrist"]['coordinate'])
        left_wrist_angle = find_triangle_angle(lelbow_to_lindex, lwrist_to_lelbow, lindex_to_lwrist)
        joint_angles['left wrist'] = left_wrist_angle

        # Right Wrist
        rwrist_to_relbow = m.dist(pose["right wrist"]['coordinate'], pose["right elbow"]['coordinate'])
        relbow_to_rindex = m.dist(pose["right elbow"]['coordinate'], pose["right index"]['coordinate'])
        rindex_to_rwrist = m.dist(pose["right index"]['coordinate'], pose["right wrist"]['coordinate'])
        right_wrist_angle = find_triangle_angle(rwrist_to_relbow, relbow_to_rindex, rindex_to_rwrist)
        joint_angles['right wrist'] = right_wrist_angle

        # Add hip rotation eventually
        # Left Hip
        lhip_to_lknee = m.dist(pose["left hip"]['coordinate'], pose["left knee"]['coordinate'])
        lknee_to_lshoulder = m.dist(pose["left knee"]['coordinate'], pose["left shoulder"]['coordinate'])
        lshoulder_to_lhip = m.dist(pose["left shoulder"]['coordinate'], pose["left hip"]['coordinate'])
        left_hip_angle = find_triangle_angle(lknee_to_lshoulder, lhip_to_lknee, lshoulder_to_lhip)
        joint_angles['left hip'] = left_hip_angle

        # Add hip rotation eventually
        # Right Hip
        rhip_to_rknee = m.dist(pose["right hip"]['coordinate'], pose["right knee"]['coordinate'])
        rknee_to_rshoulder = m.dist(pose["right knee"]['coordinate'], pose["right shoulder"]['coordinate'])
        rshoulder_to_rhip = m.dist(pose["right shoulder"]['coordinate'], pose["right hip"]['coordinate'])
        right_hip_angle = find_triangle_angle(rknee_to_rshoulder, rhip_to_rknee, rshoulder_to_rhip)
        joint_angles['right hip'] = right_hip_angle

        # Left Knee
        lhip_to_lknee = m.dist(pose["left hip"]['coordinate'], pose["left knee"]['coordinate'])
        lknee_to_lankle = m.dist(pose["left knee"]['coordinate'], pose["left ankle"]['coordinate'])
        lankle_to_lhip = m.dist(pose["left ankle"]['coordinate'], pose["left hip"]['coordinate'])
        left_knee_angle = find_triangle_angle(lankle_to_lhip, lhip_to_lknee, lknee_to_lankle)
        joint_angles['left knee'] = left_knee_angle

        # Right Knee
        rhip_to_rknee = m.dist(pose["right hip"]['coordinate'], pose["right knee"]['coordinate'])
        rknee_to_rankle = m.dist(pose["right knee"]['coordinate'], pose["right ankle"]['coordinate'])
        rankle_to_rhip = m.dist(pose["right ankle"]['coordinate'], pose["right hip"]['coordinate'])
        right_knee_angle = find_triangle_angle(rankle_to_rhip, rhip_to_rknee, rknee_to_rankle)
        joint_angles['right knee'] = right_knee_angle

        # Left Ankle
        lfoot_index_to_lankle = m.dist(pose["left foot index"]['coordinate'], pose["left ankle"]['coordinate'])
        lankle_to_lknee = m.dist(pose["left ankle"]['coordinate'], pose["left knee"]['coordinate'])
        lknee_to_lfoot_index = m.dist(pose["left knee"]['coordinate'], pose["left foot index"]['coordinate'])
        left_ankle_angle = find_triangle_angle(lknee_to_lfoot_index, lfoot_index_to_lankle, lankle_to_lknee)
        joint_angles['left ankle'] = left_ankle_angle

        # Right Ankle
        rfoot_index_to_rankle = m.dist(pose["right foot index"]['coordinate'], pose["right ankle"]['coordinate'])
        rankle_to_rknee = m.dist(pose["right ankle"]['coordinate'], pose["right knee"]['coordinate'])
        rknee_to_rfoot_index = m.dist(pose["right knee"]['coordinate'], pose["right foot index"]['coordinate'])
        right_ankle_angle = find_triangle_angle(rknee_to_rfoot_index, rfoot_index_to_rankle, rankle_to_rknee)
        joint_angles['right ankle'] = right_ankle_angle

        # Add torso rotation eventually
        # Torso rotation

        # Finally, append the joint angles for this frame to the current sequence
        joint_sequence['sequence'].append(joint_angles)
    # print("Length of the current joint sequence: ", len(joint_sequence['sequence']))
    return joint_sequence


# Finds the angle of a
def find_triangle_angle(a, b, c):

    A = (b**2 + c**2 - a**2) / (2 * b * c) # = cos(A)
    angle = m.acos(A) # in radians
    return m.degrees(angle)


if __name__ == "__main__":
    main()
