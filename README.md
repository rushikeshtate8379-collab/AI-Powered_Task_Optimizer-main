
# 🤖 AI-Powered Task Optimizer 

## 📌 Project Overview

AI-Powered Task Optimizer (Amdox) is an intelligent system that analyzes a user’s emotional state using Artificial Intelligence and recommends suitable tasks based on their mood.

The system detects emotions from **text input, webcam facial expressions, or manual mood selection** and then suggests productivity or wellness activities accordingly.

This project aims to improve **employee productivity, mental well-being, and work efficiency** by aligning tasks with the user’s emotional state.

---

# 🚀 Features

### 🧠 Real-Time Emotion Detection

* Detects emotions from text or webcam images.
* Recognizes emotions such as:

  * Angry
  * Sad
  * Neutral
  * Happy
  * Surprised
  * Fear
  * Disgust
  * Excited
  * Calm

### 🎛 Manual Emotion Selection

* Users can manually choose their mood.
* Helpful when AI detection is not used.

### 🗂 Task Recommendation System

* Suggests tasks based on detected emotion.

Example:

Emotion: Sad
Suggested Tasks:

* Take a short break
* Light documentation work
* Listen to calming music

### 📊 Mood History Tracking

* Stores emotion logs in `data/mood_history.csv`.
* Helps analyze emotional trends over time.

### 👥 Team Mood Analytics

* Aggregates team emotional data.
* Helps organizations understand team productivity and morale.

### ⚠️ Stress Detection Alerts

* Detects prolonged negative emotions.
* Can notify HR or managers if stress levels remain high.

### 🔒 Data Privacy

* Stores only anonymous information:

  * Timestamp
  * Emotion
  * Source
  * Confidence score

No personal identity data is stored.

---

# 🧩 Input Modes

| Mode             | Description                                      |
| ---------------- | ------------------------------------------------ |
| Text Input       | Users type their feelings and AI detects emotion |
| Webcam Detection | Real-time facial emotion detection               |
| Manual Selection | Users select emotion from dropdown               |

---

# ⚙️ Technologies Used

* Python
* Streamlit
* OpenCV
* Machine Learning
* Natural Language Processing
* TensorFlow / Keras
* Pandas & NumPy

---

# 📂 Project Structure

```
AI-Powered_Task_Optimizer
│
├── app.py
├── app1.py
├── Emotion Analysis Using Images.ipynb
├── Emotion Analysis Using Text.ipynb
├── tweet_emotions.csv
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/yourusername/AI-Powered_Task_Optimizer.git
```

### 2️⃣ Navigate to the project folder

```
cd AI-Powered_Task_Optimizer
```

### 3️⃣ Install required libraries

```
pip install -r requirements.txt
```

### 4️⃣ Run the Streamlit application

```
streamlit run app.py
```

---

# 📊 Data Storage

The system stores mood tracking data in:

```
data/mood_history.csv
```

This file keeps records of:

* Timestamp
* Emotion detected
* Source of input
* Confidence score

---

# 🔮 Future Improvements

* Voice emotion detection
* AI chatbot for productivity guidance
* Advanced mood analytics dashboard
* Multi-language emotion detection
* Integration with wellness applications
* Privacy-preserving federated learning

---

# 🙌 Acknowledgements

* Emotion Analysis Using Text – NLP models
* Emotion Analysis Using Images – Facial Emotion Recognition
* Streamlit – Web application framework

---

# 👨‍💻 Author

**Rushikesh Padmakar Tate**
B.Tech CSE (AI & ML)

Project: AI-Powered Task Optimizer
