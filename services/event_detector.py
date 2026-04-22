class EventDetector:

    @staticmethod
    def detect(objects, fire):
        events = []

        if fire:
            events.append("FIRE")

        if "person" in objects:
            events.append("PERSON")

        return events