import cv2
import numpy as np
import time

# Initialize the video capture object
cap = cv2.VideoCapture(0)

# Allow the camera to warm-up and capture the background
time.sleep(2)
ret, background = cap.read()

# Flip the background image horizontally
background = np.flip(background, axis=1)

# Define the range of color to detect (in this case, red cloak)
lower_red = np.array([0, 120, 70])     # Lower bound for red color
upper_red = np.array([10, 255, 255])   # Upper bound for red color

lower_red2 = np.array([170, 120, 70])  # Secondary lower bound for red color
upper_red2 = np.array([180, 255, 255]) # Secondary upper bound for red color

while(cap.isOpened()):
    ret, frame = cap.read()

    if not ret:
        break

    # Flip the frame horizontally (mirror view)
    frame = np.flip(frame, axis=1)

    # Convert the current frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create masks to detect the red color in the frame
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

    # Combine the masks
    mask = mask1 + mask2

    # Perform morphological transformations to clean the mask
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8))

    # Invert the mask to get the part of the frame without the cloak
    mask_inverse = cv2.bitwise_not(mask)

    # Segment the cloak part out of the frame
    cloak_part = cv2.bitwise_and(background, background, mask=mask)

    # Segment the rest of the frame (without the cloak)
    non_cloak_part = cv2.bitwise_and(frame, frame, mask=mask_inverse)

    # Combine the two parts (cloak replaced by the background)
    output_frame = cv2.addWeighted(cloak_part, 1, non_cloak_part, 1, 0)

    # Display the output frame
    cv2.imshow("Invisibility Cloak", output_frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()
