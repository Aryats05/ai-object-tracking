# AI Object Tracking

An AI-powered object tracking project built using Python, YOLO, and ByteTrack.

## 🚀 Overview

This project uses a pretrained YOLO model to detect and track objects in videos.

The system identifies objects, draws bounding boxes, and assigns tracking IDs to follow objects across video frames.

## 🧠 Technologies

- Python
- YOLO
- Ultralytics
- ByteTrack
- OpenCV

## 🔄 Pipeline

Video
↓
YOLO Object Detection
↓
ByteTrack Object Tracking
↓
Bounding Boxes + Tracking IDs
↓
Output Video

## 📁 Project Structure

```text
ai-object-tracking/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── videos/
```

## ⚙️ Installation

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## ▶️ Usage

Place a video named `people.mp4` inside the `videos` folder.

Run:

```bash
python main.py
```

The first run downloads the pretrained YOLO model. The program displays the tracked video and saves the output.

## 🧠 What I Learned

- Object detection
- Object tracking
- YOLO and ByteTrack
- Bounding boxes and tracking IDs
- Video processing with OpenCV
- Pretrained AI models

## 🔮 Future Improvements

- People counting
- Vehicle tracking
- Movement analysis
- Real-time video analytics
- Integration with FastAPI