import cv2
import numpy as np

pts = []
def mouseClick(event, xPos, yPos, flags, param):
    global pts

    if event == cv2.EVENT_LBUTTONDOWN:
        pts.append([xPos, yPos])
        print(pts)
        
path = "Desktop/build/cards.jpg"
frame = cv2.imread(path)
cv2.namedWindow('FRAME')
cv2.setMouseCallback('FRAME', mouseClick)

while True:
    cv2.imshow('FRAME', frame)
    
    if len(pts) >= 4:
        pts_src = np.float32(pts[:4])
        pts_dst = np.float32([[0, 0], [200, 0], [200, 400], [0, 400]])
        matrix = cv2.getPerspectiveTransform(pts_src, pts_dst)
        warped = cv2.warpPerspective(frame, matrix, (200, 400))
        
        cv2.imshow('Warped', warped)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
