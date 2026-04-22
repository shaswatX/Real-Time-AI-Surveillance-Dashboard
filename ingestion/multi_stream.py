import cv2

class MultiStream:
    def __init__(self, video_paths):
        self.video_paths = video_paths
        self.caps = []

        for path in video_paths:
            cap = cv2.VideoCapture(path)
            self.caps.append(cap)

    def read_frames(self):
        frames = []

        for idx, cap in enumerate(self.caps):

            if not cap.isOpened():
                cap.open(self.video_paths[idx])

            ret, frame = cap.read()

            # if video ended, restart
            if not ret:
                cap.release()
                self.caps[idx] = cv2.VideoCapture(self.video_paths[idx])
                ret, frame = self.caps[idx].read()

            if ret:
                frames.append(frame)
            else:
                frames.append(None)

        return frames