import cv2
import numpy as np
from deepface import DeepFace
from tensorflow.keras.models import load_model

# Load the trained emotion recognition model
emotion_model = load_model("emotion_recognition_model.h5")

# Emotion labels
emotion_labels = ['anger', 'happy', 'sad', 'neutral']

# Load cascade classifiers
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to detect emotions in frame
def detect_emotions(frame):
    # Convert frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Extract face features
        face_roi = gray_frame[y:y + h, x:x + w]

        # Resize features to match model input shape
        resized_face = cv2.resize(face_roi, (48, 48), interpolation=cv2.INTER_AREA)

        # Normalize resized face image
        normalized_face = resized_face / 255.0

        # Reshape image to match input shape of the model
        reshaped_face = normalized_face.reshape(1, 48, 48, 1)  # Ensure input has a single channel

        # Detect emotion
        preds = emotion_model.predict(reshaped_face)
        emotion_idx = np.argmax(preds)
        emotion = emotion_labels[emotion_idx]

        # Draw rectangle around face and label with detected emotion
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(frame, emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    return frame

# Turn on camera
cap = cv2.VideoCapture(0)

while True:
    # Get the frames
    ret, frame = cap.read()

    if not ret:
        break

    # Detect emotions in frame
    frame_with_emotions = detect_emotions(frame)

    # Display frame with emotions
    cv2.imshow('Emotion Detection', frame_with_emotions)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close all windows
cap.release()
cv2.destroyAllWindows()
