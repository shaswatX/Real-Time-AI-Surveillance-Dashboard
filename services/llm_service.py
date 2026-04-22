class LLMService:

    @staticmethod
    def generate_alert(event, objects):
        return f"Detected {objects}. Situation: {event}"