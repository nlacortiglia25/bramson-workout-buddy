# Bramson — AI Motivational Gym Buddy

**Bramson** is a virtual workout buddy that watches your workouts in realtime and gives you personalized motivation and feedback relevant to your current workout.
Bramson allows for user specified tones and personalities, i.e. You can have your workout buddy to be informative, aggressive, friendly, neutral, or sweet. You could also have them talk formally or use some gym-brah style slang.

*Important Notes* - This repo is still under development. The program was developed in a windows environment, as of right now there may be unresolved issues with web cam integration running the program on Linux, macOS, and other operating systems. 

*Warning* - Aggressive personality may use profanity. Use are your own discretion.

This repository contains:
   - Scripts used to extract relevant features from exercise videos.
   - Scripts used to train exercise prediction models using the extracted exercise data using KNN or Random Forest.
   - Modules for pose estimation, exercise classification, message generation, and text-to-speach.
   - Light version of MediaPipe Pose Landmark model for pose estimation (may include a download script for this later to lighten repo).
   - Soon, repo will include download scripts to download a pretrained model to be used with the program.
---

## How It Works  
1. **Exercise Classification**  
   - Processes live video feed (via webcam).  
   - Uses [MediaPipe Pose Landmarker](https://ai.google.dev/edge/mediapipe/solutions/vision/pose_landmarker) and a random forest model to predict which exercise the user is performing.

2. **Motivation Generation**
   - Generates an informative or motivation message for the user, based on the exercise of the user, and user specified tones and personality.
   - Functionality soon to be added for LLM natural language generation and counting reps, the program currently uses a data set of pregenerated responses.

3. **Text-to-Speech Module**  
   - Converts motivational text into speech.  
   - Plays audio through your speakers in real-time.  

--- 
<picture>
  <!-- Dark mode image -->
  <source media="(prefers-color-scheme: dark)" srcset="./assets/dark-data-flow-image.png">
  <!-- Light mode image -->
  <source media="(prefers-color-scheme: light)" srcset="./assets/light-data-flow-image.png">
  <!-- Fallback image (if neither matches) -->
  <img alt="Bramson Data Pipeline image" src="dark-data-flow-image.png">
</picture>
---

## Features  

- Real-time pose detection using MediaPipe.  
- Exercise classification using a Random Forest model.  
- Relevant motivational or informative phrase generation.  
- Text-to-Speech integration for a full “gym buddy” effect.  
- Modular pipeline — each component (classifier, motivation generation, TTS) has limited dependency and can be improved independently.  

---

## Current Status  

- ✅ Exercise classification working through live webcam feed.  
- ✅ Model training pipeline built with extracted joint angle features.  
- ✅ Motivation generator based on predicted exercise and user defined personality.  
- ✅ Text-to-Speech module.  

---

## Roadmap  

- [ ] Improve exercise classification by considering more features and improving temporal analysis.
- [ ] Improve model training process, possibly use a CNN or another Deep Learning model. 
- [ ] Expand capabilities of motivation generator module, currently limited in personality and phrase variation. 
- [ ] Deploy for Windows and Linux Systems, as well as raspberry pi's and possibly mobile devices.

---

## Development  

Clone the repository and install dependencies:  

```bash
git clone https://github.com/nlacortiglia25/bramson-workout-buddy.git
cd bramson-workout-buddy
```

(Optional but recommended) Activate python virtual environment:
```bash
# Create a virtual environment
python -m venv venv

# Windows (PowerShell):
venv\Scripts\Activate.ps1

# Windows (Command Prompt):
venv\Scripts\activate.bat

# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

Run the live webcam demo:  

```bash
python src/streamLandmarker.py
```

---
