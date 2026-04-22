from ultralytics import YOLO

class YOLOModel:
    def __init__(self):
        self.model = YOLO("yolov8n.pt")  # lightweight

    def detect(self, frame):
        results = self.model(frame, verbose=False)
        detections = []

        for r in results:
            for box in r.boxes:
                cls = int(box.cls[0])
                label = self.model.names[cls]
                detections.append(label)

        return list(set(detections))