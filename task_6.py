import cv2
path = "Desktop/build/waterfall.webp"
image = cv2.imread(path)
size = image.shape
width = size[0]
height = size[1]
center = (int(height/2),int(width/2))
M = cv2.getRotationMatrix2D(center, 380, 1)
imageRot = cv2.warpAffine(image, M, (height, width))
cv2.imshow("Output",image)
cv2.imshow("Rotate",imageRot)
cv2.waitKey()
cv2.destroyAllWindows()