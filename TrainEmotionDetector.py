import numpy as np
import tensorflow as tf
import os
import cv2
from tensorflow.keras import layers, models
from sklearn.model_selection import train_test_split


def preprocess_data():
    X = []
    y = []
    label_map = {'angry': 0, 'happy': 1, 'sad': 2, 'neutral': 3}
    data_dir = "C:/Users/pawan/Downloads/emo/data/train"
    for emotion_label in os.listdir(data_dir):
        emotion_dir = os.path.join(data_dir, emotion_label)
        label = label_map.get(emotion_label)
        if label is None:
            continue
        for filename in os.listdir(emotion_dir):
            img_path = os.path.join(emotion_dir, filename)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            if img is not None:
                img = cv2.resize(img, (48, 48))
                img = img / 255.0
                X.append(img)
                y.append(label)
    X = np.array(X)
    y = np.array(y)
    return X, y

# Load and preprocess the data
X, y = preprocess_data()

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)




# Define the model architecture
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(48, 48, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(4, activation='softmax')  # 4 emotions: angry, happy, neutral, sad
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)

# Save the trained model
model.save("emotion_recognition_model.h5")

# Evaluate the model
test_loss, test_acc = model.evaluate(X_test, y_test)
print('Test accuracy:', test_acc)
