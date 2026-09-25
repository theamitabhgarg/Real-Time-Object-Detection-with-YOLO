# Real-Time Object Detection with YOLO and OpenCV

A real-time computer vision application that uses YOLO11, OpenCV, and PyTorch to detect, classify, and count objects from a webcam feed. The application uses CUDA GPU acceleration when an NVIDIA GPU is available.

## Features

- Real-time object detection
- Bounding box visualization
- Object class identification
- Confidence score display
- Class-wise object counting
- Total object counting
- FPS monitoring
- CUDA GPU acceleration
- Webcam-based processing

## Tech Stack

- Python
- OpenCV
- Ultralytics YOLO11
- PyTorch
- CUDA

## How It Works

The application captures frames from the webcam using OpenCV and passes them to a pretrained YOLO11 object detection model.

YOLO processes each frame and returns the detected object's class, confidence score, and bounding box coordinates.

OpenCV then visualizes the detections and displays the object counts, FPS, and processing device.

### Processing Pipeline

    Webcam
       |
       v
    OpenCV Video Capture
       |
       v
    YOLO11 Object Detection
       |
       v
    Detection Results
       |
       +-- Object Class
       +-- Confidence Score
       +-- Bounding Box
       |
       v
    Object Counting
       |
       v
    FPS Calculation
       |
       v
    OpenCV Visualization

## GPU Acceleration

The application automatically checks whether CUDA is available.

If an NVIDIA GPU with CUDA support is available, YOLO performs inference on the GPU. Otherwise, the application falls back to the CPU.

Example:

    Using device: cuda:0
    GPU: NVIDIA GeForce GTX 1650

## Installation

### 1. Clone the repository

    git clone https://github.com/theamitabhgarg/Real-Time-Object-Detection-with-YOLO.git

### 2. Navigate to the project

    cd Real-Time-Object-Detection-with-YOLO

### 3. Create a virtual environment

    python -m venv venv

### 4. Activate the virtual environment

Windows PowerShell:

    .\venv\Scripts\Activate.ps1

### 5. Install dependencies

    pip install -r requirements.txt

## Run the Application

    python main.py

The YOLO11n model will be downloaded automatically by Ultralytics during the first run if it is not already available locally.

Press Q to exit the application.

## Output

The application displays:

- Bounding boxes around detected objects
- Object class names
- Confidence scores
- Class-wise object counts
- Total number of detected objects
- Current FPS
- Processing device

Example:

    Detected Objects

    person: 2
    cell phone: 1
    bottle: 1

    Total Objects: 4
    FPS: 28.5
    Device: cuda:0

## Project Structure

    Real-Time-Object-Detection-with-YOLO/
    |
    +-- main.py
    +-- requirements.txt
    +-- .gitignore
    +-- README.md

The virtual environment and YOLO model files (*.pt) are excluded from Git using .gitignore.

## Model

This project uses YOLO11n, a lightweight YOLO model designed for real-time object detection.

Input:
Webcam frames

Output:
Object classes, confidence scores, and bounding box coordinates.

## Learning Objectives

This project was built to gain practical experience with:

- Computer vision
- Object detection
- YOLO inference
- Bounding boxes
- Confidence scores
- Object counting
- Real-time video processing
- FPS calculation
- OpenCV visualization
- PyTorch
- CUDA GPU acceleration

## Future Improvements

- Object tracking with unique IDs
- Line-crossing detection
- Entry and exit statistics
- People counting
- Video file input
- Multi-camera support
- Real-time analytics
- NVIDIA DeepStream integration

## License

This project is intended for educational and learning purposes.