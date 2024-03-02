# Importing the necessary libraries
import cv2
from simple_facerec import SimpleFacerec  # Assuming SimpleFacerec is a custom face recognition module

# Initialize SimpleFacerec for face recognition
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")  # Load encoded faces from a specified folder

# Initialize camera capture
cap = cv2.VideoCapture(1)  # 0 represents the default camera, you can change it to a different camera index if necessary

while True:
    # Capture a frame from the camera
    ret, frame = cap.read()

    # Check if frame is captured successfully
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Detect faces in the captured frame and recognize known faces
    face_locations, face_names = sfr.detect_known_faces(frame)

    # Loop through each detected face and its corresponding recognized name
    for face_loc, name in zip(face_locations, face_names):
        # Extract coordinates of the bounding box around the face
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        # Draw text label showing the name above the face
        cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)

        # Draw bounding box around the face
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

    # Display the frame with detected faces
    cv2.imshow("Frame", frame)

    # Check for key press to exit the loop
    key = cv2.waitKey(1)
    if key == 27:  # 'ESC' key
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
#            __
#           / _)
#    .-^^^-/ /
# __/       /
#<__.|_|-|_|
