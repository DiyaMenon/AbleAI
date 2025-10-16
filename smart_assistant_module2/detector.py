from ultralytics import YOLO
import cv2

def load_model():
    model = YOLO("yolov8m.pt")
    return model

def detect_objects(model, frame, conf_thresh=0.5):
    results = model(frame, stream=True, conf=conf_thresh)
    detections = []
    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            label = model.names[cls]
            conf = float(box.conf[0])
            detections.append((label, conf))
    return detections