# Bramson — AI Motivational Gym Bro

**Bramson** is your virtual workout buddy that not only recognizes your exercises in real time but also hypes you up with relevant personalized motivational phrases — just like your gym bro would.
The agent allows for user specified tones and personalities, i.e. You can have your gym bro to be informative, aggressive, friendly,  or sweet :) You could also have them talk formally or use
some gym-brah slang.

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

## System Architecture  

Here’s the high-level architecture of Bramson:  

<picture>
  <!-- Dark mode image -->
  <source media="(prefers-color-scheme: dark)" srcset="./assets/dark-data-flow-image.png">
  <!-- Light mode image -->
  <source media="(prefers-color-scheme: light)" srcset="./assets/light-data-flow-image.png">
  <!-- Fallback image (if neither matches) -->
  <img alt="Demo Screenshot" src="dark-data-flow-image.png">
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

- [ ] Improve exercise classification by including temporal sequence data.  
- [ ] Expand motivational phrase library.  
- [ ] Add personalization (e.g., user-defined workout plans, preferred motivation style).  
- [ ] Deploy as a desktop or mobile application.  

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
