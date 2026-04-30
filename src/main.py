import json
from detector import detect_landmarks
from angle import calculate_shoulder_angle, classify_angle
from visualizer import draw_output

INPUT_PATH = "../data/input/person.jpg"
OUTPUT_PATH = "../data/output/annotated.jpg"


def main():
    points, image = detect_landmarks(INPUT_PATH)

    if points is None:
        print("No person detected")
        return

    angle = calculate_shoulder_angle(points["left_shoulder"], points["right_shoulder"])

    status = classify_angle(angle)

    draw_output(image, points, OUTPUT_PATH)

    result = {"landmarks": points, "shoulder_angle": round(angle, 2), "status": status}

    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
