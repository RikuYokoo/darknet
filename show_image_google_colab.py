import cv2
import matplotlib.pyplot as plt

img = cv2.imread("predictions.jpg")
img_rgb = img[:, :, [2, 1, 0]]

plt.imshow(img_rgb)
