import cv2
import numpy as np
def mouseClick(event,xPos,yPos,flags,param):
 print(event,xPos,yPos,flags,param)
frame = np.zeros((500,500), np.uint8)
cv2.namedWindow('FRAME') 
cv2.setMouseCallback('FRAME',mouseClick)
while True:
 cv2.imshow('FRAME',frame) 
 if cv2.waitKey(1) & 0xff == ord('q'):
  break # to quit press 'q'

cv2.destroyAllWindows()