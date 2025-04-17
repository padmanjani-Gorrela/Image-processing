import cv2
path = "Desktop/build/naruto.jpeg"
image = cv2.imread(path)
cv2.imshow("Output",image)
cv2.waitKey()
cv2.destroyAllWindows()