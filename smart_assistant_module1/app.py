import cv2
import argparse
import sys, os, re
sys.path.append(os.path.dirname(os.path.abspath(__file__)))  # 👈 add this line
from ocr_reader import ocr_from_image
from speaker import speak
import pytesseract

# If you're on Windows and tesseract is not in PATH, set path here:
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def capture_from_camera(save_path='captured.jpg'):
    cap = cv2.VideoCapture(0)   # change 0 → 1 if black screen
    if not cap.isOpened():
        print("❌ ERROR: Could not open webcam.")
        return None

    print("Press SPACE to capture, ESC to exit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('Camera - Press SPACE to capture', frame)
        key = cv2.waitKey(1) & 0xFF
        if key == 27:  # ESC
            cap.release()
            cv2.destroyAllWindows()
            return None
        elif key == 32:  # SPACE
            cv2.imwrite(save_path, frame)
            cap.release()
            cv2.destroyAllWindows()
            return frame

def load_image(path):
    img = cv2.imread(path)
    if img is None:
        print("❌ ERROR: Cannot read image:", path)
    return img

def main():
    parser = argparse.ArgumentParser(description="Module 1: Read text from image and speak it")
    parser.add_argument('--mode', choices=['camera', 'file'], default='camera',
                        help='Use camera or file input')
    parser.add_argument('--file', help='Path to image file (if mode=file)')
    parser.add_argument('--lang', default='eng', help='Tesseract language code, e.g. eng, hin')
    args = parser.parse_args()

    # Get image
    if args.mode == 'camera':
        img = capture_from_camera()
        if img is None:
            print("No image captured. Exiting.")
            sys.exit(0)
    else:
        if not args.file:
            print("Please provide --file <path> when using mode=file")
            sys.exit(1)
        img = load_image(args.file)
        if img is None:
            sys.exit(1)

    # Run OCR
    print("\n🔍 Running OCR...")
    raw_text = ocr_from_image(img, lang=args.lang)
    print("\n🧾 Raw OCR output:")
    print(repr(raw_text))  # shows hidden/unprintable chars

    # Clean up the text before speaking
    text = re.sub(r'[^a-zA-Z0-9\s.,!?]', '', raw_text)   # remove weird characters
    text = ' '.join(text.split())                        # collapse newlines/spaces
    print("\n🧹 Cleaned text:", repr(text))

    # Speak out the result
    if text.strip():
        print("\n✅ Detected text:\n", text)
        speak("I found the following text.")
        speak(text)
    else:
        print("\n⚠️ No readable text detected.")
        speak("Sorry, I could not detect any readable text.")

if __name__ == '__main__':
    main()
