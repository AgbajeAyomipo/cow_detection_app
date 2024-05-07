import cv2
from ultralytics import YOLO
import time
import os

# Load the YOLOv8 model
model = YOLO(f'resources/models/best.pt')
model.to('cuda')

# Open the video file
video_path = "rtsp://admin:1313Risco@@156.67.21.177:5554/cam/realmonitor?channel=1&subtype=1"
cap = cv2.VideoCapture(video_path)

# Get the frame rate of the video
fps = cap.get(cv2.CAP_PROP_FPS)

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if not success:
        break

    annotated_frame = frame.copy()

    results  = None

    try:
        # Run YOLOv8 inference on the frame
        start_time = time.time()
        results = model(frame, device = '0')
        end_time = time.time()

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Calculate and print fps
        processing_time = end_time - start_time
        actual_fps = 1 / processing_time

        # Add FPS text on the frame
        cv2.putText(annotated_frame, f"FPS: {actual_fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    except Exception as e:
        print('Skipping frame due to error',  e)
        break

    # Display the annotated frame
    cv2.imshow("YOLOv8 Inference", annotated_frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()
