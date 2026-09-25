\# Real-Time Object Detection with YOLO and OpenCV



A real-time computer vision application that uses YOLO and OpenCV to detect and count objects from a webcam feed.



\## Features

\* Real-time object detection

\* Bounding box visualization

\* Object class identification

\* Confidence score display

\* Real-time object counting

\* FPS monitoring

\* Webcam-based processing



\## Tech Stack

\* Python

\* OpenCV

\* Ultralytics YOLO



\## How It Works

The application captures frames from the webcam and passes them to a pretrained YOLO object detection model. YOLO identifies objects in each frame and returns:

\* Object class

\* Confidence score

\* Bounding box coordinates



OpenCV then visualizes the detections and displays the number of detected objects and current FPS.



```text

Webcam ↓

OpenCV ↓

YOLO Object Detection ↓

Bounding Boxes + Classes + Confidence ↓

Object Counting ↓

OpenCV Visualization

```



\## Installation



1\. \*\*Clone the repository:\*\*

&#x20;  ```bash

&#x20;  git clone https://github.com

&#x20;  ```



2\. \*\*Navigate to the project:\*\*

&#x20;  ```bash

&#x20;  cd real-time-object-detection

&#x20;  ```



3\. \*\*Create a virtual environment:\*\*

&#x20;  ```bash

&#x20;  python -m venv venv

&#x20;  ```



4\. \*\*Activate it on Windows:\*\*

&#x20;  ```powershell

&#x20;  .\\venv\\Scripts\\Activate.ps1

&#x20;  ```



5\. \*\*Install dependencies:\*\*

&#x20;  ```bash

&#x20;  pip install -r requirements.txt

&#x20;  ```



\## Run the Application

```bash

python main.py

```

\*The YOLO model will be downloaded automatically the first time the application is executed. Press \*\*Q\*\* to exit.\*



\## Project Structure

```text

real\_time\_object\_detection/

│

├── main.py

├── requirements.txt

├── .gitignore

└── README.md

```



\## Future Improvements

\* Object tracking with unique IDs

\* Line-crossing based counting

\* Entry and exit statistics

\* Class-specific counting

\* Video file input

\* Object tracking visualization

\* Multi-camera support



\## Learning Objectives

This project was built to understand practical computer vision concepts including:

\* Object detection

\* Bounding boxes

\* Confidence scores

\* YOLO inference

\* Real-time video processing

\* Object counting

\* FPS calculation

\* OpenCV visualization



\## License

This project is intended for educational and learning purposes.



