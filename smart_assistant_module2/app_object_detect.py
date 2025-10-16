import cv2
from detector import load_model, detect_objects
from speaker import speak

def main():
    print("🔍 Loading YOLO model...")
    model = load_model()
    print("✅ Model ready. Starting camera...")

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("❌ Cannot open camera.")
        return

    seen_objects = set()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        detections = detect_objects(model, frame)
        for (label, conf) in detections:
            if conf > 0.6:
                # Draw box & label (optional)
                cv2.putText(frame, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 
                            1, (0, 255, 0), 2, cv2.LINE_AA)
                # Speak new objects only once
                if label not in seen_objects:
                    seen_objects.add(label)
                    print(f"🧠 Detected: {label} ({conf:.2f})")
                    speak(f"I see a {label}")

        cv2.imshow("Smart Assistant - Object Detection", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == 27:  # ESC to quit
            break

    cap.release()
    cv2.destroyAllWindows()
    print("👋 Exited")

if __name__ == "__main__":
    main()