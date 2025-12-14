# Real-Time Computer Vision System with MQTT

This project implements a real-time computer vision AI module designed to be integrated into distributed IoT systems using the MQTT protocol.

The system receives images from external devices (such as ESP32, IP cameras, or other system modules), processes visual information, and generates automatic decisions based on facial recognition and object detection.

# Project Objective

To develop a decoupled AI inference service capable of:

Receiving images in real time via MQTT

Verifying whether a face is authorized or not

Detecting relevant objects (people and animals)

Operating as an independent module within an IoT architecture

This approach allows the system to scale easily and integrate with other components without tight coupling.

# Core Features
## Facial Recognition

Uses the face_recognition library to extract facial embeddings.

Compares incoming images against a previously authorized reference face.

## The system outputs:

✅ AUTHORIZED if the face matches

❌ DENIED if it does not match or if no face is detected


# Object Detection (YOLOv8)

Integrates the YOLOv8 model for object detection in images.

Detects specific classes such as:

person

dog

Reports detected objects along with their confidence scores.

# MQTT Communication

The system acts as an MQTT subscriber client.

Receives Base64-encoded images from a defined topic.

Easily integrates with:

Embedded devices (ESP32)

Other backend services

Storage systems such as MongoDB / GridFS

# Project Structure
├── recibidor_mqtt.py      # Main AI service (MQTT subscriber)
├── publicador.py          # Test client that publishes images
├── utils.py               # Image encoding/decoding utilities
├── prueba.jpg             # Authorized reference face image
├── yolov8n.pt             # Pretrained YOLOv8 model
├── requirements.txt       # Project dependencies
└── README.md

# Technologies Used

Python

MQTT (Mosquitto)

face_recognition / dlib

OpenCV

YOLOv8 (Ultralytics)

NumPy

# How to Run the Project Locally
1️.Start the MQTT broker
mosquitto

2️. Install dependencies
pip install -r requirements.txt

3️.Run the AI module
python recibidor_mqtt.py


The system will remain listening for incoming images.

4️.Send a test image
python publicador.py

## Expected Output

The AI module console will display messages such as:

🔐 AUTHORIZED ✅

❌ DENIED

🟢 Detected: person (0.98)

⚠️ No relevant objects detected


# Role and Personal Contribution

In this project, I was responsible for:

Designing the AI inference module

Implementing facial recognition logic

Integrating YOLOv8 for object detection

Enabling real-time communication via MQTT

Developing a decoupled and reusable system architecture