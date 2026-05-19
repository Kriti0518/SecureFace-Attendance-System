# SecureFace Attendance System

SecureFace Attendance System is a Python and OpenCV based project that helps automate attendance using real-time face detection through a webcam.

This project captures face images, detects faces live using OpenCV, and stores attendance records in CSV format automatically.

## Features

- Real-time webcam face detection
- Automatic attendance marking
- CSV attendance record system
- Easy and simple interface
- OpenCV based detection

## Technologies Used

- Python
- OpenCV
- NumPy
- CSV

## Files Included

- secureface.py → Main project file
- dataset_creator.py → Captures face images
- face_recognition_engine.py → Face detection system
- attendance_manager.py → Handles attendance records
- attendance_records.csv → Stores attendance data
- face_dataset/ → Stores captured images

## How to Run

Install required libraries:

```bash
pip install -r requirements.txt
python secureface.py
