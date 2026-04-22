import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

import streamlit as st
import cv2
from streamlit_autorefresh import st_autorefresh

from surveillance_app.ingestion.multi_stream import MultiStream
from surveillance_app.models.yolo_model import YOLOModel
from surveillance_app.models.fire_model import FireDetector

st.set_page_config(layout="wide", page_title="AI Surveillance Lite")

st.title("🎯 AI Surveillance Dashboard")

# slower refresh for weak hardware
count = st_autorefresh(interval=1200, key="refresh")

video_paths = [
    "data/cam1.mp4",
    "data/cam2.mp4",
    "data/cam3.mp4"
]

if "stream" not in st.session_state:
    st.session_state.stream = MultiStream(video_paths)

if "model" not in st.session_state:
    st.session_state.model = YOLOModel()

stream = st.session_state.stream
model = st.session_state.model

frames = stream.read_frames()

cols = st.columns(3)

alerts = []
detect_cam = count % 3   # only one camera inference each cycle

for i, frame in enumerate(frames):
    with cols[i]:
        st.subheader(f"CAM {i+1}")

        if frame is None:
            st.warning("No Feed")
            continue

        frame = cv2.resize(frame, (320, 240))
        st.image(frame, channels="BGR", width="stretch")

        if i == detect_cam:
            objects = model.detect(frame)
            fire = FireDetector.detect(frame)

            st.write("Objects:", objects)

            if fire:
                alerts.append(f"🔥 Fire in CAM {i+1}")

# Correlation
if len(alerts) >= 2:
    st.error("🚨 Multi-camera fire correlation")

for a in alerts:
    st.warning(a)

if not alerts:
    st.success("No threat detected")