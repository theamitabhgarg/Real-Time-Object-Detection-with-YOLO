import cv2
import time
import torch
from collections import Counter
from ultralytics import YOLO


# =========================
# Configuration
# =========================

MODEL_PATH = "yolo11n.pt"
CONFIDENCE_THRESHOLD = 0.5
CAMERA_INDEX = 0
INFERENCE_SIZE = 416

# Use GPU if CUDA is available
DEVICE = "cuda:0" if torch.cuda.is_available() else "cpu"


# =========================
# Load YOLO Model
# =========================

print(f"Using device: {DEVICE}")

if DEVICE.startswith("cuda"):
    print(f"GPU: {torch.cuda.get_device_name(0)}")

model = YOLO(MODEL_PATH)


# =========================
# Open Webcam
# =========================

cap = cv2.VideoCapture(CAMERA_INDEX)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()


# Set webcam resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


# =========================
# FPS Variables
# =========================

previous_time = 0


# =========================
# Main Loop
# =========================

while True:

    success, frame = cap.read()

    if not success:
        print("Error: Could not read frame.")
        break

    # Get frame dimensions
    frame_height, frame_width = frame.shape[:2]

    # Run YOLO inference
    results = model(
        frame,
        imgsz=INFERENCE_SIZE,
        conf=CONFIDENCE_THRESHOLD,
        device=DEVICE,
        verbose=False
    )

    # Store detected object names
    detected_objects = []

    # =========================
    # Process Detections
    # =========================

    for result in results:

        boxes = result.boxes

        for box in boxes:

            confidence = float(box.conf[0])
            class_id = int(box.cls[0])
            class_name = model.names[class_id]

            # Get bounding box coordinates
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            # Make sure bounding box stays inside frame
            x1 = max(0, min(x1, frame_width - 1))
            y1 = max(0, min(y1, frame_height - 1))
            x2 = max(0, min(x2, frame_width - 1))
            y2 = max(0, min(y2, frame_height - 1))

            # Add object to list
            detected_objects.append(class_name)

            # Draw bounding box
            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            # =========================
            # Draw Label
            # =========================

            label = f"{class_name} {confidence:.2f}"

            label_y = y1 - 10

            # If label would go above the frame,
            # place it inside the bounding box instead.
            if label_y < 25:
                label_y = y1 + 25

            # Don't allow label to go outside the frame
            label_y = min(label_y, frame_height - 10)

            cv2.putText(
                frame,
                label,
                (x1, label_y),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

    # =========================
    # Count Objects
    # =========================

    object_counts = Counter(detected_objects)

    total_objects = len(detected_objects)


    # =========================
    # Calculate FPS
    # =========================

    current_time = time.time()

    if previous_time != 0:
        fps = 1 / (current_time - previous_time)
    else:
        fps = 0

    previous_time = current_time


    # =========================
    # Information Panel
    # =========================

    # Calculate panel height dynamically
    panel_height = 150 + (len(object_counts) * 25)

    # Keep panel inside frame
    panel_height = min(panel_height, frame_height - 20)

    cv2.rectangle(
        frame,
        (10, 10),
        (280, panel_height),
        (0, 0, 0),
        -1
    )

    # Title
    cv2.putText(
        frame,
        "Detected Objects",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    # =========================
    # Object List
    # =========================

    y_position = 70

    for object_name, count in object_counts.items():

        text = f"{object_name}: {count}"

        cv2.putText(
            frame,
            text,
            (20, y_position),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )

        y_position += 25


    # =========================
    # Statistics
    # =========================

    cv2.putText(
        frame,
        f"Total Objects: {total_objects}",
        (20, y_position + 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"FPS: {fps:.1f}",
        (20, y_position + 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"Device: {DEVICE}",
        (20, y_position + 70),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2
    )


    # =========================
    # Display Frame
    # =========================

    cv2.imshow(
        "Real-Time Object Detection",
        frame
    )


    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


# =========================
# Cleanup
# =========================

cap.release()
cv2.destroyAllWindows()

print("Application closed.")