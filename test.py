import cv2
path = "Desktop/build/naruto.jpeg"
image = cv2.imread(path)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Output",image)
cv2.imshow("Output_gray",image_gray)
cv2.imwrite('Desktop/build/naruto.jpeg',image_gray)
cv2.waitKey()
cv2.destroyAllWindows()