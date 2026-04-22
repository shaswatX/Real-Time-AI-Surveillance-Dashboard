import cv2
import numpy as np

class FireDetector:

    @staticmethod
    def detect(frame):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # fire-like HSV range
        lower = np.array([0, 120, 180])
        upper = np.array([35, 255, 255])

        mask = cv2.inRange(hsv, lower, upper)

        # percentage of fire-colored pixels
        fire_pixels = cv2.countNonZero(mask)
        total_pixels = frame.shape[0] * frame.shape[1]

        fire_ratio = fire_pixels / total_pixels

        # stricter threshold
        if fire_ratio > 0.0009:
            return True

        return False