import numpy as np


def calculate_shoulder_angle(left, right):
    x1, y1 = left
    x2, y2 = right

    angle_rad = np.arctan2(y2 - y1, x2 - x1)
    angle_deg = abs(np.degrees(angle_rad))

    return angle_deg


def classify_angle(angle):
    if angle <= 3:
        return "Normal"
    else:
        return "Deviation Detected"
