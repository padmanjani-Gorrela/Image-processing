import cv2
import mediapipe as mp
cam = cv2.VideoCapture("Desktop/build/Screen Recording 2024-07-27 142727.mp4")
mp_faces = mp.solutions.face_detection
face_detection = mp_faces.FaceDetection()

while True:
    ret, frame = cam.read() 
    if not ret:
        break  

    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  
    faceResults = face_detection.process(frameRGB)  
    if faceResults.detections: 
        height, width, _ = frame.shape
        for face in faceResults.detections:
            bBox = face.location_data.relative_bounding_box 
            x, y, w, h = (
                int(bBox.xmin * width),
                int(bBox.ymin * height),
                int(bBox.width * width),
                int(bBox.height * height)
            )
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2) 
    
    cv2.imshow('Webcam', frame) 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()  
cv2.destroyAllWindows()
