import cv2
path = "Desktop/build/ball.jpg"
image = cv2.imread(path)
edges = cv2.Canny(image,200,300)
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL,
cv2.CHAIN_APPROX_NONE)
contoured = image.copy()
cv2.drawContours(contoured, contours, -1, (50, 3,50), 3)

cv2.imshow("Output",image)
cv2.imshow("Edges",contoured)
cv2.waitKey()

cv2.destroyAllWindows()