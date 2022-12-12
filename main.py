import cv2

# Load the video from the camera
video = cv2.VideoCapture(0)

# Loop over each frame of the video
while True:
    # Read the current frame from the video
    _, frame = video.read()

    # Use OpenCV to detect traffic signals in the frame
    signals = detect_signals(frame)

    # Loop over each detected signal
    for signal in signals:
        # Classify the signal as a violation or non-violation
        violation = classify_signal(signal)

        # If the signal is a violation, highlight it on the frame
        if violation:
            highlight_violation(frame, signal)

    # Display the resulting frame with violations highlighted
    cv2.imshow('Frame', frame)

    # Check if the user pressed the 'q' key to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and destroy the windows
video.release()
cv2.destroyAllWindows()
