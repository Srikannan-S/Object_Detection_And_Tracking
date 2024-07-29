import cv2
import numpy as np

# Load your image (replace 'kaffee.png' with your image file)
in_image = 'LensBox.jpg'

# Read the image and convert it to HSV
frame = cv2.imread(in_image)
frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# Define the region of interest (ROI) where you want to sample the color
# For example, if you want to sample the entire image, use the entire frame
# Calculate the minimum and maximum HSV values within the ROI
h_min, s_min, v_min = np.min(frameHSV, axis=(0, 1))
h_max, s_max, v_max = np.max(frameHSV, axis=(0, 1))

print(f"Low HSV values: Hue={h_min:.2f}, Saturation={s_min:.2f}, Value={v_min:.2f}")
print(f"High HSV values: Hue={h_max:.2f}, Saturation={s_max:.2f}, Value={v_max:.2f}")




