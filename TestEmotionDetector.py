import os
import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Function to load images and their corresponding labels
def load_images_from_folder(folder):
    images = []
    labels = []
    label_map = {'angry': 0,'happy': 1, 'sad': 2, 'neutral': 3}
    for emotion_label in os.listdir(folder):
        emotion_dir = os.path.join(folder, emotion_label)
        label = label_map.get(emotion_label)
        if label is None:
            continue
        for filename in os.listdir(emotion_dir):
            img_path = os.path.join(emotion_dir, filename)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            if img is not None:
                img = cv2.resize(img, (48, 48))
                img = img / 255.0
                images.append(img)
                labels.append(label)
    return np.array(images), np.array(labels)

# Load and preprocess the test data
X_test, y_test = load_images_from_folder("C:/Users/pawan/Downloads/emo/data/test")

# Load the trained model
model = load_model("emotion_recognition_model.h5")

# Evaluate the model on the test data
test_loss, test_acc = model.evaluate(X_test, y_test)
print('Test accuracy:', test_acc)
