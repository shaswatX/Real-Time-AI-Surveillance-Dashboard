````markdown
# AI Surveillance Lite Dashboard

A lightweight real-time multi-camera surveillance system built with Python, Streamlit, OpenCV, and YOLOv8 Nano.

Designed for CPU systems and low-RAM laptops.

## Features

- 3 camera live dashboard
- Real-time object detection
- Fire detection alerts
- Multi-camera correlation alerts
- Lightweight and fast
- No GPU required

---

## Tech Stack

- Python
- Streamlit
- OpenCV
- YOLOv8 Nano

---

## Project Structure

```bash
ai-surveillance-system/
│
├── surveillance_app/
│   ├── dashboard/
│   │   └── streamlit_app.py
│   │
│   ├── ingestion/
│   │   └── multi_stream.py
│   │
│   ├── models/
│   │   ├── yolo_model.py
│   │   └── fire_model.py
│   │
│   ├── services/
│   │   ├── event_detector.py
│   │   └── correlation_engine.py
│   │
│   └── __init__.py
│
├── data/
│   ├── cam1.mp4
│   ├── cam2.mp4
│   └── cam3.mp4
│
├── requirements.txt
└── README.md
````

---

## Installation

```bash
git clone https://github.com/yourusername/ai-surveillance-system.git
cd ai-surveillance-system
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / Mac

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Project

```bash
streamlit run surveillance_app/dashboard/streamlit_app.py
```

Open browser:

```text
http://localhost:8501
```

---

## Input Videos

Place videos inside:

```bash
data/
```

Example:

```bash
cam1.mp4
cam2.mp4
cam3.mp4
```

If only one video available:

```python
video_paths = ["data/cam1.mp4"] * 3
```

---

## Hardware Friendly

Optimized for:

* CPU only systems
* 6GB RAM laptops
* No GPU required

---

## Future Improvements

* Real CCTV RTSP feeds
* Face recognition
* Intrusion detection
* Smoke detection model
* Kafka streaming
* Email alerts

---

## Author

Shaswat Shekhar Panda

```
```
