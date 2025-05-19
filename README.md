# Face Recognition Attendance System

A comprehensive attendance management system that uses facial recognition with anti-spoofing protection, offering both desktop GUI and web interfaces.

## Description

This system provides a modern solution for attendance tracking using facial recognition technology. It features:

### Core Technology
- **Face Recognition**: Uses the `face_recognition` library powered by dlib for accurate face detection and recognition
- **Anti-Spoofing**: Implements Silent Face Anti-Spoofing to prevent fake face attacks using photos or videos
- **Real-time Processing**: Processes video feeds in real-time for immediate recognition

### Dual Interface
1. **Desktop Application**
   - Native GUI built with tkinter
   - Live webcam feed display
   - Intuitive button controls
   - Pop-up notifications for actions
   - Local database management

2. **Web Interface**
   - Browser-based access
   - Responsive design
   - Cross-platform compatibility
   - Real-time video processing
   - RESTful API backend

### Data Management
- **User Registration**: Store face encodings and images
- **Attendance Logging**: Timestamp-based entry/exit tracking
- **Database Structure**: Local file-based storage for portability
- **Log Format**: CSV-style logging with name, timestamp, and action

### Security Features
- **Anti-Spoofing Detection**: Prevents photo/video-based attacks
- **Real-time Validation**: Ensures live presence
- **Secure Storage**: Protected face encoding storage
- **Input Validation**: Checks for face presence and quality

![Anti-Spoofing Framework](Silent-Face-Anti-Spoofing-master/images/framework.jpg)
*Framework of the Silent Face Anti-Spoofing system used in this project*

## Prerequisites

1. Install Python requirements:
```bash
pip install -r requirements.txt
```

2. Set up dlib on Windows (if needed):
   Follow the guide at: https://medium.com/analytics-vidhya/how-to-install-dlib-library-for-python-in-windows-10-57348ba1117f

## System Requirements

### Hardware
- Webcam with minimum 720p resolution
- 4GB RAM minimum (8GB recommended)
- Processor: Intel i3/AMD equivalent or better
- Storage: 500MB free space

### Software
- Windows 10/11 or Linux
- Python 3.8 or higher
- Modern web browser (for web interface)
- Proper lighting conditions for optimal face detection

## Project Structure

```
Face-Recognition+Attendance-System/
├── api.py              # FastAPI backend server
├── main.py            # Desktop GUI application
├── util.py            # Utility functions
├── start_all.py       # Web interface starter
├── static/            # Web interface files
│   └── webcam_client.html
├── db/                # User face database
└── log.txt           # Attendance logs
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/KarimTahaM/Face-Recognition-Attendance-System
cd Face-Recognition-Attendance-System
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Download anti-spoofing models:
```bash
git clone https://github.com/minivision-ai/Silent-Face-Anti-Spoofing.git
```

## Usage

### Desktop GUI Version
```bash
python main.py
```

### Web Interface Version
```bash
python start_all.py
```
This will:
1. Start the FastAPI backend server on http://localhost:8000
2. Start a web server for the frontend on http://localhost:8080
3. Automatically open the web interface in your default browser

## Features Usage

1. **Registration**:
   - Click "Register New User"
   - Enter your name
   - Look directly at the camera
   - Click "Accept"

2. **Login**:
   - Click "Login"
   - Look at the camera
   - System will recognize and log your entry

3. **Logout**:
   - Click "Logout"
   - Look at the camera
   - System will recognize and log your exit

## Best Practices

1. **Registration**:
   - Ensure good lighting
   - Look directly at camera
   - Maintain neutral expression
   - Remove glasses if possible
   - Keep ~60cm distance from camera

2. **Daily Use**:
   - Maintain consistent lighting
   - Face camera directly
   - Stay within frame
   - Wait for confirmation message

## Troubleshooting

Common issues and solutions:

1. **Face Not Detected**
   - Check lighting conditions
   - Adjust distance from camera
   - Ensure face is clearly visible
   - Remove face coverings

2. **Recognition Issues**
   - Re-register in better lighting
   - Update face encoding
   - Clear database and start fresh
   - Check camera focus

3. **System Performance**
   - Close unnecessary applications
   - Check camera connection
   - Restart application
   - Update Python packages

## Logs

Attendance logs are stored in `log.txt` with the following format:
```
name,timestamp,action
```
Where action is either "in" or "out"

## Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Open pull request

## Acknowledgments

- face_recognition library
- Silent Face Anti-Spoofing project
- FastAPI framework
- OpenCV community

## Support

For issues and feature requests, please use the GitHub issues tracker.
