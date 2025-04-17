import cv2
import numpy as np

# Input video file
cam = cv2.VideoCapture('Desktop/build/waterfall.webp')

while True:
    _, frame = cam.read()
    
    # Converting to HSV for masking
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Lower and upper bound for color
    lowerBound = np.array([110, 80, 134])
    upperBound = np.array([150, 255, 255])
    
    mask = cv2.inRange(frameHSV, lowerBound, upperBound)

    # Finding contours on masked frame
    ballContours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # If multiple set of contours available, iterate through each
    for ballContour in ballContours:
        area = cv2.contourArea(ballContour)
        if area > 500:  # Filter out noise
            x, y, w, h = cv2.boundingRect(ballContour)  # This function returns the x, y coordinates and the width and height of the rectangle
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Draw rectangle

    cv2.imshow('mask', mask)
    cv2.imshow('Ball', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()  # To quit the camera press 'q'
