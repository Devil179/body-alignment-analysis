import cv2
import mediapipe as mp

mp_pose = mp.solutions.pose


def detect_landmarks(image_path):
    pose = mp_pose.Pose(static_image_mode=True)

    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    results = pose.process(image_rgb)

    if not results.pose_landmarks:
        return None, image

    h, w, _ = image.shape
    landmarks = results.pose_landmarks.landmark

    def get_point(idx):
        return int(landmarks[idx].x * w), int(landmarks[idx].y * h)

    points = {
        "left_shoulder": get_point(mp_pose.PoseLandmark.LEFT_SHOULDER),
        "right_shoulder": get_point(mp_pose.PoseLandmark.RIGHT_SHOULDER),
        "left_hip": get_point(mp_pose.PoseLandmark.LEFT_HIP),
        "right_hip": get_point(mp_pose.PoseLandmark.RIGHT_HIP),
        "nose": get_point(mp_pose.PoseLandmark.NOSE),
    }

    return points, image
