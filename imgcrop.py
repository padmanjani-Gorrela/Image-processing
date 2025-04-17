import cv2
start_point = None
end_point = None
cropping = False
def mouse_crop(event, x, y, flags, param):
    global start_point, end_point, cropping, image
 
    if event == cv2.EVENT_LBUTTONDOWN:
        start_point = (x, y)
        cropping = True
  
    elif event == cv2.EVENT_MOUSEMOVE:
        if cropping:
            end_point = (x, y)

    elif event == cv2.EVENT_LBUTTONUP:
        end_point = (x, y)
        cropping = False
 
        if start_point and end_point:
            roi = image[start_point[1]:end_point[1], start_point[0]:end_point[0]]
            cv2.imshow("Cropped Image", roi)
            cv2.imwrite("cropped_image.jpg", roi)
            print("Cropped image saved as 'cropped_image.jpg'")

image = cv2.imread("Desktop/build/bean.webp")
clone = image.copy()

cv2.namedWindow("Image")
cv2.setMouseCallback("Image", mouse_crop)

while True:
    display_image = image.copy()
    if start_point and end_point and cropping:
        cv2.rectangle(display_image, start_point, end_point, (0, 255, 0), 2)
    cv2.imshow("Image", display_image)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
