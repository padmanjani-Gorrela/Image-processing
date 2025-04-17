import cv2
import numpy as np

image_path = 'Desktop/build/cards.jpg'
image = cv2.imread(image_path)

if image is None:
    print(f"Error: Could not load image at {image_path}")
    exit()

edited_image = image.copy()

def update_image(x):
    global edited_image
    edited_image = image.copy()

    # Apply color map filter
    colormap = cv2.getTrackbarPos('Filter', 'Editor')
    if colormap < 12:
        edited_image = cv2.applyColorMap(image, colormap)

    # Zoom the image
    zoom_level = cv2.getTrackbarPos('Zoom', 'Editor') / 10.0
    if zoom_level != 0:
        height, width = image.shape[:2]
        new_dim = (int(width * zoom_level), int(height * zoom_level))
        edited_image = cv2.resize(edited_image, new_dim)

    # Rotate the image
    angle = cv2.getTrackbarPos('Rotate', 'Editor')
    height, width = edited_image.shape[:2]
    center = (width // 2, height // 2)
    matrix = cv2.getRotationMatrix2D(center, angle, 1)
    edited_image = cv2.warpAffine(edited_image, matrix, (width, height))

    # Blur the image
    blur_amount = cv2.getTrackbarPos('Blur', 'Editor')
    if blur_amount > 0:
        edited_image = cv2.GaussianBlur(edited_image, (2*blur_amount+1, 2*blur_amount+1), 0)

    # Sketch effect
    if cv2.getTrackbarPos('Sketch', 'Editor'):
        gray = cv2.cvtColor(edited_image, cv2.COLOR_BGR2GRAY)
        inv_gray = 255 - gray
        blurred = cv2.GaussianBlur(inv_gray, (21, 21), 0)
        sketch = cv2.divide(gray, 255 - blurred, scale=256.0)
        edited_image = cv2.cvtColor(sketch, cv2.COLOR_GRAY2BGR)

    cv2.imshow('Editor', edited_image)

# Create a window
cv2.namedWindow('Editor')

# Create trackbars
cv2.createTrackbar('Filter', 'Editor', 0, 11, update_image)
cv2.createTrackbar('Zoom', 'Editor', 10, 20, update_image)
cv2.createTrackbar('Rotate', 'Editor', 0, 360, update_image)
cv2.createTrackbar('Blur', 'Editor', 0, 20, update_image)
cv2.createTrackbar('Sketch', 'Editor', 0, 1, update_image)

# Mouse callback for cropping
cropping = False
roi = [0, 0, 0, 0]

def mouse_crop(event, x, y, flags, param):
    global cropping, roi, edited_image
    if event == cv2.EVENT_LBUTTONDOWN:
        cropping = True
        roi[0], roi[1] = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if cropping:
            roi[2], roi[3] = x, y
            temp_image = edited_image.copy()
            cv2.rectangle(temp_image, (roi[0], roi[1]), (roi[2], roi[3]), (0, 255, 0), 2)
            cv2.imshow('Editor', temp_image)
    elif event == cv2.EVENT_LBUTTONUP:
        cropping = False
        roi[2], roi[3] = x, y
        if roi[2] > roi[0] and roi[3] > roi[1]:
            cv2.rectangle(edited_image, (roi[0], roi[1]), (roi[2], roi[3]), (0, 255, 0), 2)
            cv2.imshow('Editor', edited_image)

cv2.setMouseCallback('Editor', mouse_crop)

# Display the initial image
update_image(0)

while True:
    cv2.imshow('Editor', edited_image)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('s'):
        if roi[2] > roi[0] and roi[3] > roi[1]:
            cropped_image = image[roi[1]:roi[3], roi[0]:roi[2]]
            cv2.imwrite('cropped_image.jpg', cropped_image)
            print("Cropped image saved as 'cropped_image.jpg'.")

cv2.destroyAllWindows()
