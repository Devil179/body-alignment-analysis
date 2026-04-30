# 🧍 Body Landmark Detection & Shoulder Alignment Analysis

## 📌 Overview

This project uses **MediaPipe Pose** to detect human body landmarks from an image and performs **geometric analysis** to determine shoulder alignment.

It calculates the **angle between shoulders** and classifies posture as:

* ✅ Normal (≤ 3° deviation)
* ⚠️ Deviation Detected (> 3°)

---

## 🧠 Features

* Detects 33 body landmarks using MediaPipe
* Extracts key points:

  * Nose
  * Left & Right Shoulders
  * Left & Right Hips
* Computes shoulder alignment angle using vector math
* Draws annotated output using OpenCV
* Generates structured JSON output

---

## 🛠️ Tech Stack

* Python 3.11
* MediaPipe
* OpenCV
* NumPy

---

## 📁 Project Structure

```
body-alignment-analysis/
│
├── data/
│   ├── input/
│   │   └── person.jpg
│   └── output/
│       └── annotated.jpg
│
├── src/
│   ├── detector.py
│   ├── angle.py
│   ├── visualizer.py
│   └── main.py
│
├── requirements.txt
├── README.md
```

---

## ⚙️ Installation

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

```bash
cd src
python main.py
```

---

## 🖼️ Sample Input

Place a standing human image here:

```
data/input/person.jpg
```

---

## 📊 Sample Output (Terminal)

```json
{
    "landmarks": {
        "left_shoulder": [420, 210],
        "right_shoulder": [600, 220],
        "left_hip": [430, 400],
        "right_hip": [590, 410],
        "nose": [510, 120]
    },
    "shoulder_angle": 3.18,
    "status": "Deviation Detected"
}
```

---

## 🖼️ Output Image

Annotated image is saved at:

```
data/output/annotated.jpg
```

---

## 🧮 Angle Calculation

The shoulder angle is computed using:

```
θ = arctan((y₂ - y₁) / (x₂ - x₁))
```

Or in LaTeX:

$$\theta = \arctan\left(\frac{y_2 - y_1}{x_2 - x_1}\right)$$

Where:

* `(x₁, y₁)` = Left shoulder coordinates
* `(x₂, y₂)` = Right shoulder coordinates
* `θ` = Shoulder alignment angle in degrees

---

## Demo
<img width="1920" height="911" alt="image" src="https://github.com/user-attachments/assets/fbdeba2f-c0cf-4d52-a40b-c3f04a4624e7" />


## 🚀 Future Improvements

* Add real-time webcam analysis
* Build a Flask API
* Add posture correction suggestions
* Extend to full-body joint analysis

---

## 📌 Author

Sparsh Agarwal
