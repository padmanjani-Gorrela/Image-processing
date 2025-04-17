import cv2
import numpy as np
import matplotlib.pyplot as plt
image_path = 'Desktop/build/professor.jpg'
img = cv2.imread(image_path)

if img is None:
    raise FileNotFoundError("The specified image file was not found.")

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_blurred = cv2.medianBlur(img_rgb, 3)

def create_lut(levels):
    lut = np.zeros(256, dtype=np.uint8)
    step = 256 // levels
    for i in range(256):
        lut[i] = (i // step) * step + step // 2
    return lut

levels = 8 
lut = create_lut(levels)
posterized_img = cv2.LUT(img_blurred, lut)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(img_rgb)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Posterized Image")
plt.imshow(posterized_img)
plt.axis('off')

plt.show()
