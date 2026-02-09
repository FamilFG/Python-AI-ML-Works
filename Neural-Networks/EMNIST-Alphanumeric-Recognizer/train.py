import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.utils import to_categorical
from utils_emnist import load_images, load_labels, fix_orientation

BASE = "emnist/byclass/"

X_train = load_images(BASE + "emnist-byclass-train-images-idx3-ubyte")
y_train = load_labels(BASE + "emnist-byclass-train-labels-idx1-ubyte")

X_test = load_images(BASE + "emnist-byclass-test-images-idx3-ubyte")
y_test = load_labels(BASE + "emnist-byclass-test-labels-idx1-ubyte")

X_train = fix_orientation(X_train) / 255.0
X_test  = fix_orientation(X_test) / 255.0

y_train = to_categorical(y_train, 62)
y_test  = to_categorical(y_test, 62)

model = Sequential([
    Conv2D(32, (3,3), activation="relu", input_shape=(28,28,1)),
    MaxPooling2D(2,2),

    Conv2D(64, (3,3), activation="relu"),
    MaxPooling2D(2,2),

    Flatten(),
    Dense(128, activation="relu"),
    Dropout(0.5),
    Dense(62, activation="softmax")
])

model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

model.fit(
    X_train,
    y_train,
    epochs=10,
    batch_size=128,
    validation_data=(X_test, y_test)
)

model.save("C:\\Users\\ufml\\Desktop\\works\\Python-AI-ML-Works\\Neural-Networks\\EMNIST-Alphanumeric-Recognizer\\model\\emnist_cnn.keras")
print("Model saved to model/emnist_cnn")
