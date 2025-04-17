import cv2
import numpy as np
import matplotlib.pyplot as plt
image_path = 'Desktop/build/professor.jpg' 
image = cv2.imread(image_path)

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

blurred_image = cv2.medianBlur(image_rgb, 7) 
plt.figure(figsize=(10, 5))

# Original Image
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image_rgb)
plt.axis('off')

# Blurred Image
plt.subplot(1, 2, 2)
plt.title('Blurred Image')
plt.imshow(blurred_image)
plt.axis('off')

plt.show()
