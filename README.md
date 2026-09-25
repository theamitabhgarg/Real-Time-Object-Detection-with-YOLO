Real-Time Object Detection with YOLO and OpenCV



A real-time computer vision application that uses YOLO and OpenCV to detect and count objects from a webcam feed.



Features



Real-time object detection



Bounding box visualization



Object class identification



Confidence score display



Real-time object counting



FPS monitoring



Webcam-based processing



Tech Stack



Python



OpenCV



Ultralytics YOLO



How It Works



The application captures frames from the webcam and passes them to a pretrained YOLO object detection model.







YOLO identifies objects in each frame and returns:







Object class



Confidence score



Bounding box coordinates







OpenCV then visualizes the detections and displays the number of detected objects and current FPS.



Webcam

&#x20;  ↓

OpenCV

&#x20;  ↓

YOLO Object Detection

&#x20;  ↓

Bounding Boxes + Classes + Confidence

&#x20;  ↓

Object Counting

&#x20;  ↓

OpenCV Visualization





Installation



Clone the repository:



git clone https://github.com/theamitabhgarg/real-time-object-detection.git





Navigate to the project:



cd real-time-object-detection





Create a virtual environment:



python -m venv venv





Activate it on Windows:



.\\venv\\Scripts\\Activate.ps1





Install dependencies:



pip install -r requirements.txt





Run the Application



python main.py





The YOLO model will be downloaded automatically the first time the application is executed.







Press Q to exit.



Project Structure



real\_time\_object\_detection/

│

├── main.py

├── requirements.txt

├── .gitignore

└── README.md





Future Improvements



Object tracking with unique IDs



Line-crossing based counting



Entry and exit statistics



Class-specific counting



Video file input



Object tracking visualization



Multi-camera support



Learning Objectives



This project was built to understand practical computer vision concepts including:







Object detection



Bounding boxes



Confidence scores



YOLO inference



Real-time video processing



Object counting



FPS calculation



OpenCV visualization



License



This project is intended for educational and learning purposes.

