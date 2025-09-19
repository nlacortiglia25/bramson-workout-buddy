# Bramson — AI Motivational Gym Bro

**Bramson** is a virtual workout buddy that recognizes your exercises in real time and hypes you up with motivational phrases, while also providing helpful tips for form and execution (or not if you find that stuff annoying).
Bramson allows for user specified tones and personalities, i.e. You can have your gym bro to be informative, aggressive, friendly,  or sweet :) You could also have them talk formally or use
some gym-brah style slang.

This repository contains:
   - Scripts used to extract relevant features from exercise videos
   - Scripts used to train exercise predictoin models using the extracted exercise data
   - Modules for pose estimation, exercise classification, language generation, and text to speach
   - Also contains light version of MediaPipe Pose Landmark model for pose estimation (may include a download script for this later to lighten repo)

---

## How It Works  
1. **Exercise Classifier**  
   - Takes in live video data (via webcam).  
   - Uses [MediaPipe Pose Landmarker](https://ai.google.dev/edge/mediapipe/solutions/vision/pose_landmarker) and a random forest model to predict which exercise you’re performing.  

3. **Motivation Generator**
   - Generates message for the user, based on context, and user specified tones and personality.
   - Functionality soon to be added for counting reps.

5. **Text-to-Speech Module**  
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
- Exercise classification with scikit-learn models.  
- Dynamic motivational phrase generation.  
- Text-to-Speech integration for a full “gym buddy” effect.  
- Modular pipeline — each component (classifier, decision agent, TTS) can be improved independently.  

---

## Current Status  

- ✅ Exercise classification working on webcam feed.  
- ✅ Model training pipeline built with extracted joint angle features.  
- ✅ Motivation generator complete.  
- ✅ Text-to-Speech module complete.  

---

## Roadmap  

- [ ] Improve exercise classification with improved set of features and improved temporal analysis.  
- [ ] Expand motivational phrase library, currently limitted in personality and phrase variation. 
- [ ] Deploy for desktop, raspberry pi, and possibly mobile devices.

---

## Development  

Clone the repository and install dependencies:  

```bash
git clone https://github.com/yourusername/bramson.git
cd bramson
pip install -r requirements.txt
```

Run the live webcam demo:  

```bash
python src/streamLandmarker.py
```

---
