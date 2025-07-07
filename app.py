import streamlit as st
import cv2
import tempfile
from ultralytics import YOLO

# Load a lightweight YOLOv8 model
model = YOLO('yolov8n.pt')

st.title("Object Detection Demo")

# Sidebar controls
source = st.sidebar.radio("Video Source", ["Webcam", "Video File", "Upload"])

if source == "Webcam":
    cap = cv2.VideoCapture(0)
elif source == "Video File":
    path = st.sidebar.text_input("Path to video file", "video.mp4")
    cap = cv2.VideoCapture(path)
else:
    upload = st.file_uploader("Upload a video", type=["mp4","avi"])
    if upload:
        tmp = tempfile.NamedTemporaryFile(delete=False)
        tmp.write(upload.read())
        cap = cv2.VideoCapture(tmp.name)
    else:
        st.stop()

frame_placeholder = st.empty()

# Real-time detection loop
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    results = model.track(frame, stream=True)
    for res in results:
        for box in res.boxes:
            x1,y1,x2,y2 = map(int, box.xyxy[0])
            cls = int(box.cls[0]); conf = box.conf[0]
            label = f"{model.names[cls]} {conf:.2f}"
            cv2.rectangle(frame, (x1,y1),(x2,y2),(0,255,0),2)
            cv2.putText(frame, label, (x1, y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)
    frame_placeholder.image(frame[:,:,::-1], channels="RGB")

cap.release()
