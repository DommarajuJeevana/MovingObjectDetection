## Motion Detection System using OpenCV
A computer vision project built with Python and OpenCV that captures live webcam footage and detects motion in real time. The system identifies moving objects, draws bounding boxes around them, and displays a detection alert on the screen.

## Features
- Live webcam video capture
- Real-time motion detection
- Moving object identification
- Bounding box visualization
- Motion status display
- Image capture functionality
- Lightweight and easy to run

## Technologies Used
- Python
- OpenCV (cv2)
- Imutils

### Motion Detection
Detects movement by comparing the current frame with a reference frame and highlights moving objects with rectangles.

### Webcam Preview
Displays a live webcam feed.

### Image Capture
Captures a single image from the webcam and saves it locally.

## Installation

### Clone the Repository
```bash
git clone <repository-url>
cd motion-detection-system
```

### Install Dependencies
```bash
pip install opencv-python imutils
```

## Usage
### Run Motion Detection
```bash
python motion_detection.py
```

### Run Webcam Preview
```bash
python webcam_preview.py
```

### Capture an Image
```bash
python capture_image.py
```

Press **Q** to exit the webcam window.

## How It Works
1. Captures video from the webcam.
2. Converts frames to grayscale.
3. Applies Gaussian blur to reduce noise.
4. Compares frames to detect changes.
5. Finds contours of moving objects.
6. Draws bounding boxes around detected motion.
7. Displays "Moving Object Detected" when motion is found.
