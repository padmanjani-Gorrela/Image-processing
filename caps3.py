import cv2
import numpy as np

def find_color_range(frame):
    # Convert the frame from BGR to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Define initial bounds (adjust these values as necessary)
    lower_bound = np.array([30, 100, 100])
    upper_bound = np.array([60, 255, 255])
    
    # Create a mask based on the initial bounds
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    
    # Apply the mask to the original frame
    result = cv2.bitwise_and(frame, frame, mask=mask)
    
    # Display the mask and the result
    cv2.imshow('Mask', mask)
    cv2.imshow('Result', result)
    
    # Print the HSV bounds
    print(f'Lower Bound: {lower_bound}')
    print(f'Upper Bound: {upper_bound}')
    
    # Wait for a key press and then close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Load a frame from your image file
frame_path = 'Desktop/build/waterfall.webp'
img = cv2.imread(frame_path)

# Check if the image was loaded correctly
if img is None:
    print(f"Error: Unable to load image from path: {frame_path}")
else:
    find_color_range(img)
