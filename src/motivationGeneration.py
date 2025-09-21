# Given an exercise and a tone, generate a motivational message

def generate_motivation(exercise_type, tone):
    motivational_messages = {
    "barbell biceps curl": {
        "gym_bro": "C’mon, pump those guns! Every curl counts!",
        "sweet_supportive": "You’re doing amazing, keep those biceps growing!",
        "aggressive": "FUCK YOU, YOU’RE WEAK! SHOW ME THOSE CURLS!",
        "friendly": "Nice work! Keep curling, buddy!",
        "default": "Focus on form and complete each curl."
    },
    "bench press": {
        "gym_bro": "Push it, bro! Chest day domination!",
        "sweet_supportive": "You’ve got this, strong and steady!",
        "aggressive": "LIGHT WEIGHT, BABY! CRUSH IT!",
        "friendly": "Keep going, you’re doing great!",
        "default": "Maintain proper grip and press safely."
    },
    "chest fly machine": {
        "gym_bro": "Squeeze it, bro! Feel that chest burn!",
        "sweet_supportive": "Love how dedicated you are, keep it up!",
        "aggressive": "THAT ALL YOU GOT, PUSSY?! SQUEEZE HARDER!",
        "friendly": "Great effort, keep those flies controlled!",
        "default": "Slow, controlled reps for full chest engagement."
    },
    "deadlift": {
        "gym_bro": "Lift that weight like a beast, bro!",
        "sweet_supportive": "You’re strong, keep pulling with care!",
        "aggressive": "COME ON! PICK IT UP OR QUIT, WEAKLING!",
        "friendly": "Solid form! Keep pulling, you’ve got this!",
        "default": "Keep your back straight and lift with your legs."
    },
    "decline bench press": {
        "gym_bro": "Lower chest gains, bro! Push it!",
        "sweet_supportive": "Nice work! Every rep counts for growth!",
        "aggressive": "DROP IT AND PRESS, DON’T BE A BITCH!",
        "friendly": "Great reps! Keep going, friend!",
        "default": "Maintain a controlled motion and focus on your lower chest."
    },
    "hammer curl": {
        "gym_bro": "Hammer those arms, bro! Feel the power!",
        "sweet_supportive": "Your arms are looking strong, keep it up!",
        "aggressive": "WRAP YOUR FISTS AND CURL LIKE A BEAST!",
        "friendly": "Keep hammering those curls, buddy!",
        "default": "Keep elbows close and curl steadily."
    },
    "hip thrust": {
        "gym_bro": "Thrust it, bro! Build that posterior chain!",
        "sweet_supportive": "Excellent! Your glutes are getting stronger every rep!",
        "aggressive": "THRUST HARDER OR GET OFF THE BENCH, WEAKLING!",
        "friendly": "Nice thrusts! Keep those hips strong!",
        "default": "Focus on glute contraction and controlled motion."
    },
    "incline bench press": {
        "gym_bro": "Upper chest day, bro! Push it up!",
        "sweet_supportive": "Great work! You’re shaping that upper chest!",
        "aggressive": "PUSH IT TO THE SKY OR QUIT, LOSER!",
        "friendly": "Keep pressing, you’re doing awesome!",
        "default": "Control the bar and focus on upper chest engagement."
    },
    "lat pulldown": {
        "gym_bro": "Pull that bar, bro! Wide lats incoming!",
        "sweet_supportive": "Your back is getting stronger every rep!",
        "aggressive": "PULL HARD, STOP WIMPY REPS, PUSSY!",
        "friendly": "Good pull! Keep those lats engaged!",
        "default": "Keep your shoulders down and pull slowly to chest."
    },
    "lateral raise": {
        "gym_bro": "Raise those shoulders, bro! Get them delts!",
        "sweet_supportive": "Beautiful form! Keep building those shoulders!",
        "aggressive": "STOP SLACKING, RAISE THOSE WEIGHTS, IDIOT!",
        "friendly": "Nice and steady raises, friend!",
        "default": "Keep a slight bend in elbows and lift slowly."
    },
    "leg extension": {
        "gym_bro": "Crush those quads, bro! Lock out hard!",
        "sweet_supportive": "Strong legs, keep pushing safely!",
        "aggressive": "EXTEND OR YOU’RE TRASH, MOVE IT!",
        "friendly": "Good reps! Keep your legs strong!",
        "default": "Extend fully but control the motion back down."
    },
    "leg raises": {
        "gym_bro": "Hit those abs, bro! Legs up high!",
        "sweet_supportive": "Your core is improving every rep!",
        "aggressive": "RAISE THOSE LEGS OR GO HOME, PUSSY!",
        "friendly": "Nice work! Keep those abs tight!",
        "default": "Lift slowly and control the descent for best engagement."
    },
    "plank": {
        "gym_bro": "Hold it, bro! Core strong as steel!",
        "sweet_supportive": "You’re doing amazing! Keep holding strong!",
        "aggressive": "DROP NOW? PAThetic! HOLD THAT PLANK!",
        "friendly": "Keep that form, buddy, you got this!",
        "default": "Keep your back straight and core tight throughout."
    },
    "pull Up": {
        "gym_bro": "Pull yourself up, bro! Get those lats!",
        "sweet_supportive": "Great strength, keep going!",
        "aggressive": "CAN’T EVEN PULL? SORRY, PATHETIC!",
        "friendly": "Awesome reps! Keep climbing!",
        "default": "Engage your back and pull slowly to chin level."
    },
    "push-up": {
        "gym_bro": "Push it, bro! Chest and arms fire!",
        "sweet_supportive": "Nice work! Keep pushing safely!",
        "aggressive": "DROP DOWN? PATHETIC! PUSH HARD!",
        "friendly": "Good job! Keep those push-ups steady!",
        "default": "Keep body straight and lower slowly."
    },
    "romanian deadlift": {
        "gym_bro": "Hinge it, bro! Hamstrings on fire!",
        "sweet_supportive": "Strong form! Keep those legs healthy!",
        "aggressive": "BEND OR DIE, WEAKLING! HAMSTRINGS HURT!",
        "friendly": "Nice movement! Keep your back safe and strong!",
        "default": "Keep a straight back and hinge at the hips."
    },
    "russian twist": {
        "gym_bro": "Twist it, bro! Obliques blazing!",
        "sweet_supportive": "Great rotation! Your core is strong!",
        "aggressive": "TWIST HARDER OR YOU’RE TRASH, LOSER!",
        "friendly": "Keep twisting! You’re doing awesome!",
        "default": "Rotate slowly and control your torso."
    },
    "shoulder press": {
        "gym_bro": "Press it up, bro! Shoulders of steel!",
        "sweet_supportive": "Beautiful lift! Keep building those shoulders!",
        "aggressive": "PUSH OR QUIT! YOU’RE WEAK!",
        "friendly": "Great press! Keep those arms strong!",
        "default": "Press with control and avoid locking elbows aggressively."
    },
    "squat": {
        "gym_bro": "Go deep, bro! Legs of a champion!",
        "sweet_supportive": "Strong squat! Keep those legs growing!",
        "aggressive": "SQUAT DEEP OR GET OUT, PUSSY!",
        "friendly": "Nice form! Keep those squats steady!",
        "default": "Keep knees aligned and back straight."
    },
    "t bar row": {
        "gym_bro": "Row it, bro! Back thickness incoming!",
        "sweet_supportive": "Excellent pull! Your back strength is improving!",
        "aggressive": "ROW HARD, STOP SLACKING, LOSER!",
        "friendly": "Good job! Keep those rows controlled!",
        "default": "Keep your chest supported and pull with your back muscles."
    },
    "tricep dips": {
        "gym_bro": "Dip it, bro! Triceps on fire!",
        "sweet_supportive": "Great dips! Keep your arms strong!",
        "aggressive": "DIP OR DIE, PUSSY! PUSH THOSE TRICEPS!",
        "friendly": "Nice work! Keep dipping safely!",
        "default": "Lower slowly and push back up with controlled motion."
    },
    "tricep Pushdown": {
        "gym_bro": "Push it down, bro! Triceps blasting!",
        "sweet_supportive": "Strong pushdowns! Keep building your arms!",
        "aggressive": "PUSH HARD OR YOU’RE TRASH, BITCH!",
        "friendly": "Good reps! Keep those arms engaged!",
        "default": "Keep elbows close and push slowly for full tricep activation."
    }
}

    return motivational_messages[exercise_type][tone]