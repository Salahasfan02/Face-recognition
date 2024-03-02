 This repository provides functionalities to recognize known faces from live video streams or images, using state-of-the-art techniques in computer vision and machine learning. Leveraging the power of OpenCV and face_recognition libraries, this module enables easy integration and deployment of face recognition systems in various applications.

Features:

SimpleFacerec Class: This module includes a SimpleFacerec class designed for straightforward face recognition tasks. The class offers methods for loading known face encodings, detecting faces in frames, and recognizing known faces.

Efficient Encoding Handling: With methods to load encoding images from specified paths, this module ensures efficient handling of face encodings. It allows users to load pre-encoded face images, reducing processing time during real-time recognition.

Real-Time Face Detection: The system provides real-time face detection capabilities using OpenCV. It accurately locates faces in live video streams or frames captured from cameras, facilitating seamless integration into surveillance systems, attendance management, and more.

Facial Recognition: Leveraging the face_recognition library, this module implements robust facial recognition algorithms. It compares detected face encodings with known face encodings, enabling the identification of individuals within the captured frames.

User-Friendly Interface: The module is designed with simplicity in mind, offering a user-friendly interface for developers to integrate into their projects effortlessly. It provides clear instructions and intuitive methods for loading data and performing face recognition tasks.

Customizable: Developers can customize parameters such as frame resizing to optimize performance based on their specific requirements. Additionally, the module supports customization of recognition thresholds and other parameters to fine-tune the recognition process.


*You have to make a file name"images" and put the images of the people you need the program to recognize
