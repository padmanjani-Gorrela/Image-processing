import cv2
path = "Desktop/build/waterfall.webp"
image = cv2.imread(path)
size = image.shape
width = int(size[0]/2)
height = int(size[1]/2)
image_resize = cv2.resize(image,(height,width))
# Display image in a window
cv2.imshow("Output",image)
cv2.imshow("Resize",image_resize)
cv2.waitKey()
cv2.destroyAllWindows()