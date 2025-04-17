import cv2
path = 'Desktop/build/waterfall.webp'

image = cv2.imread(path)
imageRot = cv2.rotate(image, cv2.ROTATE_180)
cv2.imshow("Output",image)
cv2.imshow("Resize",imageRot)
cv2.waitKey()

cv2.destroyAllWindows()