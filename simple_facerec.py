# Import necessary libraries
import face_recognition
import cv2
import os
import glob
import numpy as np

# Define a class for simple face recognition
class SimpleFacerec:
    def __init__(self):
        # Initialize lists to store known face encodings and names
        self.known_face_encodings = []
        self.known_face_names = []

        # Define a parameter for resizing the frame to speed up face recognition
        self.frame_resizing = 0.25

    # Method to load encoding images from a specified path
    def load_encoding_images(self, images_path):
        """
        Load encoding images from path
        :param images_path:
        :return:
        """
        # Get file paths of images from the specified folder
        images_path = glob.glob(os.path.join(images_path, "*.*"))

        # Print the number of encoding images found
        print("{} encoding images found.".format(len(images_path)))

        # Loop through each image path
        for img_path in images_path:
            # Read the image and convert it to RGB format
            img = cv2.imread(img_path)
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # Get the filename of the image
            basename = os.path.basename(img_path)
            (filename, ext) = os.path.splitext(basename)

            # Get the face encoding of the image
            img_encoding = face_recognition.face_encodings(rgb_img)[0]

            # Store the filename and encoding in the lists
            self.known_face_encodings.append(img_encoding)
            self.known_face_names.append(filename)

        # Print a message indicating that encoding images are loaded
        print("Encoding images loaded")

    # Method to detect known faces in a frame
    def detect_known_faces(self, frame):
        # Check if the frame is valid
        if frame is None or frame.size == 0:
            print("Error: Empty frame or invalid image.")
            return [], []

        # Resize the frame
        small_frame = cv2.resize(frame, (0, 0), fx=self.frame_resizing, fy=self.frame_resizing)

        # Convert the frame to RGB format
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        # Find face locations and encodings in the frame
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        # Initialize an empty list to store names of detected faces
        face_names = []

        # Loop through each face encoding
        for face_encoding in face_encodings:
            # Compare the face encoding with known face encodings
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            name = "Unknown"

            # Find the best match for the face
            face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)

            # If a match is found, assign the corresponding name
            if matches[best_match_index]:
                name = self.known_face_names[best_match_index]
            face_names.append(name)

        # Convert face locations to match the resized frame
        face_locations = np.array(face_locations)
        face_locations = face_locations / self.frame_resizing
        return face_locations.astype(int), face_names
#            __
#           / _)
#    .-^^^-/ /
# __/       /
#<__.|_|-|_|
