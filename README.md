# ⭐ AbleAI – Multimodal On-Device AI Assistant (OCR + Object Detection + Voice Assistant)

AbleAI is a **fully offline, multimodal AI assistant** built for ARM-based devices.  
It includes three independent modules:

1. **OCR Reader** – Reads text aloud from captured images  
2. **Object Detection Assistant** – Detects objects in real time using YOLOv8  
3. **Voice Assistant** – Accepts voice commands and performs OCR or detection  

This project showcases how powerful AI can run **locally**, **privately**, and **efficiently** without cloud APIs or GPUs.

---

## 🚀 Features

### 📖 **Module 1 — OCR Reader**
- Captures images using the camera  
- Preprocesses them for better OCR accuracy  
- Extracts text using Tesseract OCR  
- Speaks the detected text via offline TTS  

### 🎯 **Module 2 — Object Detection**
- Runs YOLOv8n and YOLOv8m models on CPU  
- Fully offline object detection  
- Announces detected objects  
- Designed for ARM efficiency

### 🎙 **Module 3 — Voice Assistant**
- Offline speech-to-text  
- Can respond to commands like:  
  - “Read this text”  
  - “Describe what you see”  
- Integrates OCR, object detection, and TTS  
- Works offline end-to-end  

---

## 📂 Project Structure

```
AbleAI/
│
├── smart_assistant_module1/        # OCR Reader
│   ├── app.py
│   ├── ocr_reader.py
│   ├── speaker.py
│   └── requirements.txt
│
├── smart_assistant_module2/        # Object Detector
│   ├── app_object_detect.py
│   ├── detector.py
│   ├── speaker.py
│   ├── yolov8n.pt
│   ├── yolov8m.pt
│   └── requirements.txt
│
├── smart_assistant_module3/        # Voice Assistant
│   ├── app_voice_assistant.py
│   ├── speech_to_text.py
│   ├── speaker.py
│   └── requirements.txt
│
└── README.md
```

---

## 🔧 Installation & Setup

### 📌 **Requirements**
- Python 3.8+  
- ARM-based device (recommended)  
- Tesseract OCR installed  
- Webcam or device camera  

---

# ▶️ Running Each Module

---

## 1️⃣ **OCR Reader**

### Install dependencies:
```
cd smart_assistant_module1
pip install -r requirements.txt
```

### Run the module:
```
python app.py --mode camera
```

### Optional:
```
python app.py --mode file --file test.jpg
```

---

## 2️⃣ **Object Detection (YOLOv8)**

### Install dependencies:
```
cd smart_assistant_module2
pip install -r requirements.txt
```

### Run:
```
python app_object_detect.py
```

YOLO models included:
- `yolov8n.pt` — fast and lightweight  
- `yolov8m.pt` — more accurate  

---

## 3️⃣ **Voice Assistant**

### Install dependencies:
```
cd smart_assistant_module3
pip install -r requirements.txt
```

### Run:
```
python app_voice_assistant.py
```
 

---

## 🧠 Technologies Used

- **Python**
- **OpenCV**
- **YOLOv8 (Ultralytics)**
- **Tesseract OCR**
- **pyttsx3** offline TTS
- **SpeechRecognition**
- **NumPy**
- **Pillow**

---

## 🌱 Future Improvements

- On-device LLM for summarization  
- Multilingual OCR + translation  
- Android APK version  
- Real-time continuous reading mode  
- Memory-based conversation for assistant  

---

## ⭐ Acknowledgements

- Ultralytics YOLOv8  
- Tesseract OCR  
- OpenCV community  
- Python open-source ecosystem

---
