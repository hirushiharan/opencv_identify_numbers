"""
Program: OpenCV Identify Numbers
Author: Hirushiharan Thevendran
Created On: 01.02.2024
Last Modified On: 04.02.2024

Programe Description: Python application using the OpenCV library to identify numbers in a video stream.
File Description: Contains function to read the camera input and identify the numbers using HSV image processing.

Python Version: 3.10
"""

import cv2
import numpy as np


def identify_num(l_h, l_s, l_v, u_h, u_s, u_v):
    cap = cv2.VideoCapture(0)

    while True:
        _, frame = cap.read()

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        l_b = np.array([l_h, l_s, l_v])
        u_b = np.array([u_h, u_s, u_v])

        mask = cv2.inRange(hsv, l_b, u_b)

        res = cv2.bitwise_and(frame, frame, mask=mask)

        return res
