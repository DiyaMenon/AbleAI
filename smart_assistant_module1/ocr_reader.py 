import cv2
import pytesseract
import numpy as np

def ocr_from_image(frame, lang='eng'):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.adaptiveThreshold(
        gray, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY, 11, 2
    )
    kernel = np.ones((1, 1), np.uint8)
    processed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    processed = cv2.resize(processed, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)

    config = "--oem 3 --psm 6"
    text = pytesseract.image_to_string(processed, config=config, lang=lang)
    return text
