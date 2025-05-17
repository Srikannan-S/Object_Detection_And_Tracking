🎯 Object Detection and Tracking using HSV Color Range in OpenCV

This Python project demonstrates how to get HSV color range values from an image and perform real-time object detection and tracking using OpenCV and imutils. The detection is based on filtering colors in a specified HSV range.

🔥 Features

1. Load an image and compute minimum and maximum HSV values in the image  
2. Use HSV color range to create a mask for detecting a specific object color  
3. Real-time object detection and tracking via webcam  
4. Draw circles around detected objects and mark their centers  
5. Basic directional output based on object's position and size (e.g., Left, Right, Front, Stop)  

🚀 Technologies Used

1. Python – Programming language  
2. OpenCV – For image processing and computer vision  
3. numpy – Numerical operations on images  
4. imutils – Helper functions for image processing  

⚙️ Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/object-detection-hsv.git  
   cd object-detection-hsv
   ```

2. Install required packages:
   ```bash
   pip install opencv-python numpy imutils  
   ```
   
3. Place your input image (e.g., LensBox.jpg) in the project directory.  

4. Run the HSV value extraction script to get HSV ranges from your image:  
   ```bash
   python get_hsv_values.py  
   ```
   
5. Run the real-time object detection script:  
   ```bash
   python object_tracking.py  
   ```
   
🛠️ How It Works

- HSV Value Extraction:  
  - Loads an image and converts it to the HSV color space.  
  - Computes minimum and maximum HSV values within the entire image (or ROI).  
  - Prints out the HSV value ranges that can be used for masking colors.

- Real-Time Object Detection and Tracking:  
  - Captures video feed from the webcam.  
  - Resizes and blurs each frame to reduce noise.  
  - Converts the frame to HSV color space and creates a mask based on predefined HSV low and high ranges.  
  - Performs morphological operations (erode, dilate) on the mask to clean it.  
  - Finds contours from the mask and selects the largest contour as the detected object.  
  - Calculates the minimum enclosing circle and centroid for the detected contour.  
  - Draws a circle around the object and a dot at the centroid.  
  - Prints directional commands based on the object's position and size relative to the frame (Left, Right, Front, Stop).  
  - Displays the processed video in a window.  
  - Press 'q' to quit the program.

📂 Project Structure
```bash
📂object-detection-hsv  
├── get_hsv_values.py         # Script to extract HSV min/max values from an image  
├── object_tracking.py        # Real-time object detection and tracking script  
├── LensBox.jpg               # Sample input image for HSV extraction  
└── README.md                 # Project documentation  
```
