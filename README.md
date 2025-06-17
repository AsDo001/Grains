# 🖼️ Image Processing Project

This project showcases fundamental image processing techniques using Python, focusing on contour detection and edge detection. It leverages powerful libraries including OpenCV, scikit-image, NumPy, and Matplotlib.

## ✨ Features
- **Image Resizing**: Resizes input images to a consistent resolution
- **Active Contour Segmentation**: Implements snake algorithm for object boundary detection
- **Canny Edge Detection**: Highlights edges using Canny algorithm
- **Visualization**: Displays original images, processed results, and contours

## 📋 Prerequisites
Install required libraries:
```bash
pip install opencv-python numpy scikit-image matplotlib

## 🗂️ Project Structure

├── main.py              # Active contour segmentation
├── canny.py             # Canny edge detection
├── resize.py            # Image resizing
├── CORN_WHITE.jpg       # Sample input image
├── README.md            # Project documentation
└── LICENSE              # MIT License

## 🚀 Usage
Clone repository:
git clone <repository-url>
cd image-processing-project
Prepare input image:

Place your image in project directory (default: CORN_WHITE.jpg)

Update file paths in scripts if using different image

Run scripts:
# Active Contour Segmentation
python main.py

# Canny Edge Detection
python canny.py

# Image Resizing
python resize.py

## 🧠 Code Overview

Active Contour Segmentation (main.py)
# Key parameters
alpha = 0.015    # Contour elasticity
beta = 10.0      # Contour rigidity
gamma = 0.001    # Evolution step size
max_num_iter = 500  # Maximum iterations

Resizes image to 800x800 pixels

Applies Gaussian smoothing

Initializes circular contour at center

Visualizes initial (red dashed) and final (blue solid) contours

Canny Edge Detection (canny.py)
Resizes image to 500x500 pixels

Applies Canny algorithm with thresholds (100, 200)

Displays original and edge-detected images

Image Resizing (resize.py)
Loads image in grayscale

Resizes to 500x500 pixels

Displays resized image

## 📝 Notes
Tune active contour parameters (alpha, beta, gamma) based on image content

Adjust Canny thresholds (100, 200) for optimal edge detection

Ensure input image exists in project directory

## 📜 License
MIT License - see LICENSE file for details

## 🤝 Contributing
Contributions welcome! Submit pull requests or open issues to discuss improvements.

## Built with ❤️ using Python and OpenCV

This Markdown features:
- Clean section headers with relevant emojis
- Consistent code block formatting
- Visual directory tree structure
- Highlighted parameters and key functionality
- Clear usage instructions with copy-paste ready commands
- Responsive design for GitHub rendering
- Important notes in dedicated section
- Visual separation of components

The layout is optimized for GitHub README rendering with proper spacing, section organization, and emphasis on key information while maintaining technical accuracy.
