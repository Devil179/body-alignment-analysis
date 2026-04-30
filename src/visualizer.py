import cv2


def draw_output(image, points, output_path):
    left = points["left_shoulder"]
    right = points["right_shoulder"]

    # Draw key points
    for key, pt in points.items():
        cv2.circle(image, pt, 5, (0, 255, 0), -1)

    # Draw shoulder line
    cv2.line(image, left, right, (255, 0, 0), 2)

    cv2.imwrite(output_path, image)
