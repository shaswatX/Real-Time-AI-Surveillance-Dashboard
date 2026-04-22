from collections import defaultdict
import time

class CorrelationEngine:

    def __init__(self):
        self.events_log = defaultdict(list)

    def update(self, cam_id, events):
        timestamp = time.time()
        for e in events:
            self.events_log[e].append((cam_id, timestamp))

    def correlate(self):
        alerts = []
        current_time = time.time()

        if "FIRE" in self.events_log:
            # only recent events (last 3 sec)
            recent = [
                cam for cam, t in self.events_log["FIRE"]
                if current_time - t < 3
            ]

            unique_cams = list(set(recent))

            # 🔥 require persistence across frames
            if len(unique_cams) >= 2:
                alerts.append(f"🔥 Fire detected in multiple cameras: {unique_cams}")

        return alerts