# -*- coding: utf-8 -*-
"""
AI-Powered Employee Emotion Analyzer
"""

import streamlit as st
import cv2
import numpy as np
from PIL import Image
import speech_recognition as sr

st.set_page_config(page_title="AI Emotion Task Optimizer")

# -------------------------
# LOGIN PAGE
# -------------------------

def login_page():
    st.title("Employee Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "employee" and password == "password123":
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("Login successful!")
        else:
            st.error("Invalid login")


# -------------------------
# TASK SUGGESTION
# -------------------------

def suggest_work_based_on_emotion(emotion):

    st.subheader(f"Detected Emotion: {emotion}")

    if emotion == "Stressed":
        st.warning("You seem stressed. Take a short break.")
    elif emotion == "Neutral":
        st.info("Good time to work on routine tasks.")
    elif emotion == "Happy":
        st.success("Great mood! Try creative work.")
    else:
        st.info("Take it easy and relax a bit.")

    task = st.text_input("Task Description")
    duration = st.number_input("Task Duration (hours)", min_value=1)
    deadline = st.date_input("Deadline")

    if st.button("Assign Task"):
        st.success(f"Task '{task}' assigned for {duration} hours")


# -------------------------
# TEXT EMOTION
# -------------------------

def text_emotion():

    st.subheader("Text Emotion Detection")

    text = st.text_area("Enter text")

    if text:

        text = text.lower()

        if "happy" in text:
            emotion = "Happy"
        elif "sad" in text:
            emotion = "Sad"
        elif "stress" in text:
            emotion = "Stressed"
        else:
            emotion = "Neutral"

        suggest_work_based_on_emotion(emotion)


# -------------------------
# FACE EMOTION
# -------------------------

def face_emotion():

    st.subheader("Face Emotion Detection")

    img_file = st.camera_input("Take a picture")

    if img_file is not None:

        img = Image.open(img_file)
        img = np.array(img)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )

        faces = face_cascade.detectMultiScale(gray,1.3,5)

        for (x,y,w,h) in faces:

            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

        st.image(img)

        # dummy emotion prediction
        emotion = "Happy"

        suggest_work_based_on_emotion(emotion)


# -------------------------
# SPEECH EMOTION
# -------------------------

def speech_emotion():

    st.subheader("Speech Emotion Detection")

    r = sr.Recognizer()

    if st.button("Record Speech"):

        with sr.Microphone() as source:

            st.write("Speak now...")
            audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            st.write("You said:", text)

            if "happy" in text:
                emotion = "Happy"
            elif "sad" in text:
                emotion = "Sad"
            elif "stress" in text:
                emotion = "Stressed"
            else:
                emotion = "Neutral"

            suggest_work_based_on_emotion(emotion)

        except:
            st.error("Could not understand audio")


# -------------------------
# MAIN PAGE
# -------------------------

def main():

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        login_page()

    else:

        st.title(f"Welcome {st.session_state.username}")

        option = st.selectbox(
            "Choose Emotion Input",
            ("Text", "Face", "Speech")
        )

        if option == "Text":
            text_emotion()

        elif option == "Face":
            face_emotion()

        elif option == "Speech":
            speech_emotion()


if __name__ == "__main__":
    main()
