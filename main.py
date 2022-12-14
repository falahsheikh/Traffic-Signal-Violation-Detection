import cv2
import numpy as np

# Capture video from a camera mounted at a traffic intersection
video = cv2.VideoCapture(0)

while True:
    # Read the next frame from the video
    ret, frame = video.read()

    # Use a color filter to isolate the red pixels in the image
    red_mask = cv2.inRange(frame, (0, 0, 100), (100, 100, 255))

    # Use contour detection to find the shapes of the traffic signals
    contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the processed frame
    cv2.imshow('Traffic Signal Detection', frame)

    # Check for user input to stop the program
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

# Release the video capture object
video.release()