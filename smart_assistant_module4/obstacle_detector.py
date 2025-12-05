from ultralytics import YOLO
import cv2

def load_model():
    # small and fast model
    return YOLO("yolov8l.pt")

def detect_obstacles(model, frame):
    results = model(frame, verbose=False)
    obstacles = []

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            conf = float(box.conf[0])
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            label = model.names[cls]

            width = x2 - x1
            height = y2 - y1
            area = width * height  # proxy for closeness

            obstacles.append({
                "label": label,
                "confidence": conf,
                "area": area,
                "box": (x1, y1, x2, y2)
            })

    return obstacles
