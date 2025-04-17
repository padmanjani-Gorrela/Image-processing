import cv2
cam = cv2.VideoCapture(0)

cam.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
cam.set(cv2.CAP_PROP_FPS,15)
# Getting camera feed width and height after modifying them
width = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = cam.get(cv2.CAP_PROP_FPS)
# # for video file, use:
# cam = cv2.VideoCapture('video_file_path'

while True:
 i, frame = cam.read() # reading one frame from the camera object
 cv2.imshow('Webcam', frame) # display the current frame in a windonamed 'Webcam'
 print('resolution:',width, 'x', height, '| frames per second:', fps)
 # Waits for 1ms and check for the pressed key
 if cv2.waitKey(1) & 0xff == ord('q'):
  break # press q to quit the camera (getut of the loop)
cam.release() # close the camera
cv2.destroyAllWindows() # Close all the active windows
