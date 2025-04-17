import cv2
import numpy as np
hueLow = 0
hueHigh = 0 
satLow = 0
satHigh = 0
valLow = 0
valHigh = 0

def onTrack1(val):
    global hueLow
    hueLow = val

def onTrack2(val):
    global hueHigh
    hueHigh = val

def onTrack3(val):
    global satLow
    satLow = val

def onTrack4(val):
    global satHigh
    satHigh = val

def onTrack5(val):
    global valLow
    valLow = val

def onTrack6(val):
    global valHigh
    valHigh = val
cv2.namedWindow('Trackbars')

cv2.createTrackbar('Hue low', 'Trackbars', 0, 179, onTrack1)
cv2.createTrackbar('Hue high', 'Trackbars', 179, 179, onTrack2)
cv2.createTrackbar('Sat low', 'Trackbars', 0, 255, onTrack3)
cv2.createTrackbar('Sat high', 'Trackbars', 255, 255, onTrack4)
cv2.createTrackbar('Val low', 'Trackbars', 0, 255, onTrack5)
cv2.createTrackbar('Val high', 'Trackbars', 255, 255, onTrack6)
image = cv2.imread('Desktop/build/waterfall.webp')
if image is None:
    print("Error: Image not found")
    exit()

while True:
    frameHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lowerBound = np.array([hueLow, satLow, valLow])
    upperBound = np.array([hueHigh, satHigh, valHigh])
    mask = cv2.inRange(frameHSV, lowerBound, upperBound)
    masked = cv2.bitwise_and(image, image, mask=mask)

    cv2.imshow('Mask', mask)
    cv2.imshow('Original', image)
    cv2.imshow('Masked', masked)
    print("lowerBound: ", lowerBound)
    print("upperBound: ", upperBound)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
