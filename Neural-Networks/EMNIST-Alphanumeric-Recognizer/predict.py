import cv2
import numpy as np
from tensorflow.keras.models import load_model

def decode_label(i):
    if i < 10:
        return str(i)
    elif i < 36:
        return chr(i - 10 + ord('A'))
    else:
        return chr(i - 36 + ord('a'))

model = load_model("model/emnist_cnn.keras")

img = cv2.imread("test-images/tAv2.png", cv2.IMREAD_GRAYSCALE)

img = cv2.GaussianBlur(img, (5,5), 0)
_, img = cv2.threshold(
    img, 0, 255,
    cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
)

img = cv2.resize(img, (28,28))
img = img / 255.0
img = img.reshape(1,28,28,1)

pred = model.predict(img)
cls = np.argmax(pred)

print("Prediction:", decode_label(cls))
