# OpenCV Number Identification

## Introduction

OpenCV Number Identification is a web application that utilizes OpenCV for identifying numbers in live video streams. It allows users to adjust the HSV (Hue, Saturation, Value) values to fine-tune the image processing for better number detection.

## How it Works

The application captures video from the user's camera using the browser's `navigator.mediaDevices.getUserMedia()` API. Users can adjust the HSV values using sliders provided in the interface. When the "Number Recognition" button is clicked, the current HSV values are sent to a Flask backend via a POST request.

The Flask backend processes the video stream using OpenCV based on the provided HSV values. Once numbers are identified, the backend sends the processed video stream back to the frontend.

The frontend then displays both the input and processed video streams in separate HTML `<video>` elements, allowing users to see the real-time number identification.

## Steps to Run the Application

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/hirushiharan/opencv_identify_numbers.git
    ```

2. Navigate to the project directory:

    ```bash
    cd OpenCV-Number-Identification
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask backend server:

    ```bash
    python app.py
    ```

5. Open a web browser and go to `http://localhost:5000` to access the application.

6. Adjust the HSV values using the sliders as needed.

7. Click on the "Number Recognition" button to start identifying numbers in the video stream.

8. Observe the input and processed video streams to see the real-time number identification.

9. To stop the application, press `Ctrl + C` in the terminal where the Flask server is running.

## Requirements

- Python 3.x
- Flask
- OpenCV
- Modern web browser supporting HTML5 features (Chrome, Firefox, Safari)
