import cv2
import numpy as np

# Read the image
img = cv2.imread('Desktop/build/professor.jpg')

if img is None:
    raise FileNotFoundError("The specified image file was not found.")

img = cv2.resize(img, (800, 800))  # Resize for consistency

def posterize(img, levels=7):
    indices = np.arange(0, 256)  # Array of all colors
    divider = np.linspace(0, 255, levels + 1)[1]  # Quantization values
    quantiz = np.int32(np.linspace(280, 30, levels))  # Quantization colors
    color_levels = np.clip(np.int32(indices / divider), 0, levels - 1)  # Color levels 0, 1, 2, ..., levels-1
    palette = quantiz[color_levels]  # Creating the palette
    img2 = palette[img]  # Applying palette on image
    img2 = cv2.convertScaleAbs(img2)  # Convert back to uint8
    return img2

# Apply posterization
posterized_img = posterize(img)

# Convert to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply edge detection
edges = cv2.Canny(img_gray, 20, 20)

# Convert edges to color
edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

# Combine the posterized image and edges
cartoon_img = cv2.bitwise_and(posterized_img, edges)

# Display the result
cv2.imshow('Cartoonified Image', cartoon_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
