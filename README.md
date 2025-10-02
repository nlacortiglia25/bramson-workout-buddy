# Bramson — AI Motivational Gym Bro

**Bramson** is a virtual workout buddy that watches your workouts in realtime and gives you personalized motivation and feedback relevant to your current workout.
Bramson allows for user specified tones and personalities, i.e. You can have your workout buddy to be informative, intense, friendly, neutral, or sweet :) You could also have them talk formally or use some gym-brah style slang.

This repository contains:
   - Scripts used to extract relevant features from exercise videos.
   - Scripts used to train exercise prediction models using the extracted exercise data using KNN or Random Forest.
   - Modules for pose estimation, exercise classification, language generation, and text-to-speach.
   - Light version of MediaPipe Pose Landmark model for pose estimation (may include a download script for this later to lighten repo).
   - Soon, repo will include download scripts to download a pretrained model to be used with the program.
---

## How It Works  
1. **Exercise Classifier**  
   - Takes in live video data (via webcam).  
   - Uses [MediaPipe Pose Landmarker](https://ai.google.dev/edge/mediapipe/solutions/vision/pose_landmarker) and a random forest model to predict which exercise you’re performing.

2. **Motivation Generator**
   - Generates message for the user, based on context, and user specified tones and personality.
   - Functionality soon to be added for LLM natural language generation and counting reps.

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
- Dynamic motivational phrase generation.  
- Text-to-Speech integration for a full “gym buddy” effect.  
- Modular pipeline — each component (classifier, decision agent, TTS) can be improved independently.  

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
- [ ] Expand capabilities of motivation generator module, currently limitted in personality and phrase variation. 
- [ ] Deploy for Windows and Linux Systems, as well as raspberry pi's and possibly mobile devices.

---

## Development  

Clone the repository and install dependencies:  

```bash
git clone https://github.com/nlacortiglia25/bramson.git
cd bramson
pip install -r requirements.txt
```

Run the live webcam demo:  

```bash
python src/streamLandmarker.py
```

---
