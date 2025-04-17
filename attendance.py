import cv2
import face_recognition
import numpy as np
import datetime
import csv

# Load template images and encode them
def load_known_faces():
    known_face_encodings = []
    known_face_names = []
    
    # Add template images for known individuals
    image_files = [
        {"path": "", "name": "Friend 1"},
        {"path": "friends/friend2.jpg", "name": "Friend 2"},
        {"path": "friends/friend3.jpg", "name": "Friend 3"}
    ]
    
    for image_file in image_files:
        image = face_recognition.load_image_file(image_file["path"])
        encoding = face_recognition.face_encodings(image)[0]
        known_face_encodings.append(encoding)
        known_face_names.append(image_file["name"])
    
    return known_face_encodings, known_face_names

# Initialize known faces
known_face_encodings, known_face_names = load_known_faces()

# Initialize video capture
video_capture = cv2.VideoCapture(0)  # Change to video file path if needed

# Initialize CSV file for attendance
attendance_file = 'attendance.csv'

# Check if attendance file exists
try:
    with open(attendance_file, 'x', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Date", "Time"])
except FileExistsError:
    pass

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    # Convert frame to RGB for face recognition
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Find all face locations and face encodings in the current frame
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Compare each face encoding with known faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        # Use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

            # Log attendance
            now = datetime.datetime.now()
            date = now.strftime("%Y-%m-%d")
            time = now.strftime("%H:%M:%S")
            with open(attendance_file, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([name, date, time])

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        # Label the face
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Display the result
    cv2.imshow('Video', frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close windows
video_capture.release()
cv2.destroyAllWindows()
