import cv2
from speaker import speak
from obstacle_detector import load_model, detect_obstacles
from direction_logic import suggest_direction

def main():
    model = load_model()
    speak("Navigation module activated.")

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        frame_width = frame.shape[1]

        obstacles = detect_obstacles(model, frame)
        direction = suggest_direction(obstacles, frame_width)

        if direction == "clear":
            print("✔ Path is clear")
            continue
        
        position, distance = direction

        # SPEAK WARNINGS BASED ON POSITION + DISTANCE
        if distance == "very_close":
            speak(f"Warning! Object very close on your {position}. Step back.")
        elif distance == "close":
            speak(f"Caution, obstacle ahead on your {position}.")
        else:
            speak(f"Object detected on your {position}, but far.")

        # ESC TO EXIT
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
