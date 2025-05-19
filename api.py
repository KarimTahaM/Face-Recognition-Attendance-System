from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import StreamingResponse
import cv2
import numpy as np
import util
import datetime
import io
from fastapi.middleware.cors import CORSMiddleware
import face_recognition
import os
import pickle

import sys
sys.path.append('./Silent-Face-Anti-Spoofing-master')
from face_test import test

app = FastAPI(
    title="Face Recognition API",
    description="Upload a face image to recognize the person. Use the /recognize/ endpoint.",
    version="1.0.0",
    docs_url="/",
    redoc_url=None
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify ["http://localhost:8000"] etc.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "message": "Welcome to the Face Recognition API!",
        "usage": "Send a POST request to /recognize/ with an image file (form field name: 'file')."
    }


@app.post("/recognize/")
async def recognize(file: UploadFile = File(...)):
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    name = util.recognize(img, './db')
    # Log only if a person is recognized
    if name not in ['unknown_person', 'no_persons_found']:
        with open('log.txt', 'a') as f:
            f.write(f"{name},{datetime.datetime.now()},in\n")
    return {
        "name": name,
        "endpoint": "/recognize/"
    }


@app.post("/login_or_register/")
async def login_or_register(
    file: UploadFile = File(...),
    name: str = Form(None),
    action: str = Form(None)
):
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # Check if face is detected first
    face_locations = face_recognition.face_locations(img)
    if not face_locations:
        return {
            "status": "error",
            "message": "No face detected. Please make sure your face is clearly visible."
        }
    
    # Add anti-spoofing check
    label = test(
        image=img,
        model_dir='./Silent-Face-Anti-Spoofing-master/resources/anti_spoof_models',
        device_id=0
    )
    
    if label != 1:
        return {
            "status": "error",
            "message": "Spoof detected! Please use a real face."
        }
    
    # Handle registration case
    if name:
        # Save face encoding along with image for better recognition
        face_encoding = face_recognition.face_encodings(img, face_locations)[0]
        with open(os.path.join('./db', f'{name}_encoding.pkl'), 'wb') as f:
            pickle.dump(face_encoding, f)
        cv2.imwrite(os.path.join('./db', f'{name}.jpg'), img)
        return {
            "status": "registered",
            "message": f"Successfully registered as {name}"
        }
    
    # Continue with existing recognition logic
    recognized_name = util.recognize(img, './db')
    log_path = 'log.txt'

    # Handle logout action
    if action == 'logout':
        if recognized_name not in ['unknown_person', 'no_persons_found']:
            with open(log_path, 'a') as f:
                f.write(f"{recognized_name},{datetime.datetime.now()},out\n")
            return {
                "status": "recognized",
                "message": f"Goodbye, {recognized_name}! You have been logged out.",
                "name": recognized_name
            }
        else:
            return {
                "status": "unrecognized",
                "message": "Unknown user. Cannot log out."
            }

    # Handle normal login/register
    if recognized_name not in ['unknown_person', 'no_persons_found']:
        with open(log_path, 'a') as f:
            f.write(f"{recognized_name},{datetime.datetime.now()},in\n")
        return {
            "status": "recognized",
            "message": f"Welcome back, {recognized_name}!",
            "name": recognized_name
        }