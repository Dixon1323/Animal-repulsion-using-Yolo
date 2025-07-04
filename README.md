# Animal-Repulsion-Using-YOLO

[![Language](https://img.shields.io/badge/Language-Python-yellow.svg?style=for-the-badge)](https://en.wikipedia.org/wiki/Programming_language)

This project presents an automated system that uses **YOLO (You Only Look Once)** object detection to identify animals in real-time and trigger a repulsion mechanism. The system is designed for use in areas where wildlife intrusion poses a problem—such as agricultural fields or human-inhabited zones—and integrates both AI and IoT components.

---

## 📚 Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

---

## 🚀 Features

Based on the project structure and available files, the following features are implemented or planned:

- **Real-Time Animal Detection**:
  - Uses a custom-trained YOLO model (`best.pt`) to identify animals from a video feed (e.g., webcam, surveillance camera).

- **Automated Repulsion Mechanism**:
  - Communicates with a **NodeMCU** or similar microcontroller to activate deterrent systems (like sound alarms, lights, or water sprays).

- **Hardware Interface Support**:
  - The `nodemcu_code/` directory contains embedded C++/Arduino code for actuating external devices.

- **Modular Application Architecture**:
  - Main application (`app.py`) handles video input, detection, and interaction with the IoT subsystem.

---

## 🧰 Technologies Used

- **Python**
- **OpenCV** – Video stream processing and image handling
- **YOLOv5/v8** – Object detection model
- **PyTorch / Ultralytics** – For loading and running the model
- **Serial Communication** – For communication with microcontroller (likely via `pyserial`)
- **NodeMCU** – Wi-Fi enabled microcontroller to control the physical repulsion system
- **Arduino (ESP8266 Core)** – Used to program the NodeMCU board

Dependencies are listed in the `requirements.txt` file.

---

## ⚙️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/animal-repulsion-using-yolo.git
cd animal-repulsion-using-yolo
```

### 2. Create a Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 4. Prepare the YOLO Model
Ensure your custom model file `best.pt` is present in the root directory or wherever expected by the script (`app.py`).

---

## ▶️ Usage

### Running the Python Application
```bash
python app.py
```

This will:
- Capture video input (default: webcam)
- Detect animals using the YOLO model
- Send a signal to NodeMCU if a detection event is triggered

### Hardware Setup

- Flash the code inside `nodemcu_code/` to your NodeMCU board using the **Arduino IDE**.
- Ensure serial communication (or Wi-Fi, if implemented) is established between your Python application and the microcontroller.
- The NodeMCU will activate the repulsion mechanism (e.g., buzzer, sprinkler, etc.).

---

## 🧪 Example Workflow

1. Train or use a pre-trained YOLO model for the animals relevant to your use-case.
2. Place the system in a field/camera-monitored zone.
3. When an animal is detected:
   - The model identifies it using the YOLO framework.
   - `app.py` sends a command via serial (or wireless) to the NodeMCU.
   - NodeMCU triggers the repulsion hardware.

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a new branch:
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add AmazingFeature"
   ```
4. Push the branch:
   ```bash
   git push origin feature/AmazingFeature
   ```
5. Open a pull request

---

## 📌 Notes

- You may need to adjust your camera source in `app.py` (`cv2.VideoCapture(0)` or IP camera).
- For outdoor deployment, ensure proper casing for the NodeMCU and any repulsion hardware.
- Future improvements may include:
  - Cloud alerting via MQTT or Firebase
  - Solar-powered operation
  - Integration with cloud AI services

---
