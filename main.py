
from ultralytics import YOLO
from pathlib import Path

# Video file
video_path = Path("videos/people.mp4")

# Check that the video exists
if not video_path.exists():
    raise FileNotFoundError(
        f"Video not found: {video_path}. "
        "Check the filename inside the videos folder."
    )

# Load a pretrained YOLO model
model = YOLO("yolo11n.pt")

print("Starting object tracking...")
print("A window will open showing the tracked video.")

# Detect and track objects throughout the video
model.track(
    source=str(video_path),
    tracker="bytetrack.yaml",
    show=True,
    save=True,
    conf=0.3
)

print("Tracking completed.")
print("Check the runs/detect or runs/track folder for output.")
