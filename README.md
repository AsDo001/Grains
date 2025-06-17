Image Processing Project
This project demonstrates basic image processing techniques using Python, focusing on contour detection and edge detection. It utilizes libraries such as OpenCV, scikit-image, NumPy, and Matplotlib to process images, apply active contour segmentation, and perform edge detection using the Canny algorithm.
Features

Image Resizing: Resizes input images to a specified resolution for consistent processing.
Active Contour Segmentation: Implements the active contour (snake) algorithm to detect object boundaries in an image.
Canny Edge Detection: Applies the Canny edge detection algorithm to highlight edges in grayscale images.
Visualization: Displays original images, processed results, and contours using Matplotlib and OpenCV windows.

Prerequisites
To run this project, you need to have the following Python libraries installed:

opencv-python (OpenCV)
numpy
scikit-image
matplotlib

You can install these dependencies using pip:
pip install opencv-python numpy scikit-image matplotlib

Project Structure

metod_active_vect.py: Contains the active contour segmentation script, which loads an image, applies Gaussian smoothing, initializes a contour, and visualizes the results.
metod_Kanny.py: Implements Canny edge detection on a resized image and displays the results.
resize.py: Handles basic image resizing and displays the resized grayscale image.
CORN_WHITE.jpg: Sample input image used for processing (replace with your own image if needed).

Usage

Clone the Repository:
git clone <repository-url>
cd <repository-directory>


Prepare the Input Image:

Place an image file (e.g., CORN_WHITE.jpg) in the project directory.
Update the image file path in the scripts if using a different image.


Run the Scripts:

For active contour segmentation:python main.py

This will load the image, apply the active contour algorithm, and display the initial and final contours overlaid on the image.
For Canny edge detection:python canny.py

This will display the resized image and its Canny edge map.
For basic image resizing:python resize.py

This will display the resized grayscale image.



Code Overview
Active Contour Segmentation (main.py)

Loads an image and resizes it to 800x800 pixels.
Converts the image to grayscale and applies Gaussian smoothing.
Initializes a circular contour at the image center.
Applies the active contour algorithm with parameters:
alpha=0.015: Controls contour elasticity.
beta=10.0: Controls contour rigidity.
gamma=0.001: Step size for contour evolution.
max_num_iter=500: Maximum iterations for convergence.


Visualizes the initial and final contours using Matplotlib.

Canny Edge Detection (canny.py)

Uses a resized image (from resize_img) and applies the Canny edge detection algorithm with thresholds 100 and 200.
Displays the original and edge-detected images using OpenCV.

Image Resizing (resize.py)

Loads an image in grayscale and resizes it to 500x500 pixels.
Displays the resized image using OpenCV.

Notes

Ensure the input image (CORN_WHITE.jpg) exists in the project directory, or update the file path in the scripts.
The active contour parameters (alpha, beta, gamma) may need tuning depending on the image content.
The Canny edge detection thresholds (100, 200) can be adjusted for better edge detection results.

Example Output

Active Contour: A plot showing the original image with the initial (red dashed) and final (blue solid) contours.
Canny Edge Detection: Two windows showing the resized image and its edge map.
Image Resizing: A window displaying the resized grayscale image.

License
This project is licensed under the MIT License. See the LICENSE file for details.
Contributing
Contributions are welcome! Please submit a pull request or open an issue to discuss improvements or bugs.
