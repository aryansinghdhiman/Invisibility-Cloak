# **Invisibility Cloak Project**

## **Overview**  
The **Invisibility Cloak Project** is a creative application of computer vision techniques that creates the illusion of invisibility. By detecting a specific colored object (e.g., a red cloak) in a video feed and replacing it with a static background, the system provides a visually engaging real-time effect. This project is implemented using Python, OpenCV, and NumPy.

---

## **Features**  
- Real-time video processing.  
- Accurate color detection using HSV color space.  
- Seamless background replacement for invisibility effect.  
- Noise reduction and artifact handling using morphological transformations.  
- User-friendly implementation with minimal setup requirements.  

---

## **Requirements**  

### **Hardware**  
- A webcam or any camera capable of capturing live video.  
- A computer or laptop with moderate processing power.  

### **Software**  
- Python 3.6+  
- Required Python Libraries:
  - OpenCV (`pip install opencv-python`)
  - NumPy (`pip install numpy`)  

---

## **Setup and Installation**  

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/aryansinghdhiman/Invisibility-Cloak.git
   cd invisibility-cloak
   ```

2. **Install Dependencies**  
   Use pip to install the required libraries:  
   ```bash
   pip install opencv-python numpy
   ```

3. **Run the Program**  
   Execute the Python script:  
   ```bash
   python invisibility_cloak.py
   ```

4. **Usage**  
   - Place a red cloth in the camera's view.  
   - Ensure the background remains static during the program's execution.  
   - Press **'q'** to exit the program.

---

## **How It Works**  

1. **Background Initialization**  
   - Captures a static background image at the start of the program.  

2. **Color Detection**  
   - Converts video frames to HSV color space.  
   - Detects the specified color (red) using predefined HSV thresholds.  

3. **Masking and Noise Reduction**  
   - Applies masks to isolate the red regions.  
   - Cleans up the mask using morphological transformations (opening and dilation).  

4. **Background Replacement**  
   - Replaces detected red regions with corresponding parts of the static background.  

5. **Real-Time Display**  
   - Displays the processed frames in real time, creating the invisibility effect.  

---

## **Limitations**  
- Works best with a static background.  
- Detects only a single predefined color (red).  
- Performance may vary under different lighting conditions.  
- Struggles with dynamic environments or multiple moving objects.  

---

## **Future Enhancements**  
- Support for dynamic background handling.  
- Multi-color detection and processing.  
- Improved performance under varying lighting conditions.  
- Integration with augmented reality platforms for more applications.  

---

## **Contributors**  
- [Aryan Singh Dhiman](https://github.com/aryansinghdhiman)  

Feel free to contribute by submitting issues or creating pull requests!

---

## **License**  
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **References**  
- [OpenCV Documentation](https://docs.opencv.org)  
- [NumPy Documentation](https://numpy.org/doc/)  
- Tutorials and community forums like Stack Overflow for troubleshooting and optimization.
