import cv2
from app.ingestion.multi_stream import VideoStream
from app.models.yolo_model import YOLOModel
from app.services.event_detector import EventDetector
from app.services.llm_service import LLMService
from app.services.alert_service import AlertService


def run_pipeline(video_path):
    stream = VideoStream(video_path)
    model = YOLOModel()

    while True:
        ret, frame = stream.read_frame()
        if not ret:
            break

        objects = model.detect(frame)

        event = EventDetector.detect_event(objects)

        if event:
            alert_msg = LLMService.generate_alert(event, objects)
            AlertService.send(alert_msg)

        cv2.imshow("Surveillance", frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    stream.release()
    cv2.destroyAllWindows()