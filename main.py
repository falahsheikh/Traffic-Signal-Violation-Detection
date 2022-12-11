# Import the necessary libraries
import cv2

# Capture the video stream from a camera installed at an intersection
cap = cv2.VideoCapture(0)

# Check if the video stream is opened successfully
if not cap.isOpened():
    raise IOError("Cannot open the video stream")
# Pre-process the video frames
while True:
    # Read the next frame from the video stream
    ret, frame = cap.read()

    # Check if the frame is valid
    if not ret:
        break

    # Resize the frame to reduce the processing time
    frame = cv2.resize(frame, (640, 480))

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply smoothing to the grayscale frame
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    # Show the pre-processed frame
    cv2.imshow("Frame", gray)

    # Check if the user pressed the "q" key to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video stream
cap.release()
cv2.destroyAllWindows()
# Import the necessary libraries
import cv2
import numpy as np

# Capture the video stream from a camera installed at an intersection
cap = cv2.VideoCapture(0)

# Check if the video stream is opened successfully
if not cap.isOpened():
    raise IOError("Cannot open the video stream")
