"""
Program: OpenCV Identify Numbers
Author: Hirushiharan Thevendran
Created On: 01.02.2024
Last Modified On: 06.02.2024

Programe Description: Python application using the OpenCV library to identify numbers in a video stream.
File Description: Contains function to read the camera input and identify the numbers using HSV image processing.

Python Version: 3.10
"""

import cv2
import numpy as np
import base64


def identify_num(l_h, l_s, l_v, u_h, u_s, u_v):

    print("********************************** L_H: ", l_h)
    print("********************************** L_S: ", l_s)
    print("********************************** L_V: ", l_v)
    print("********************************** U_H: ", u_h)
    print("********************************** U_S: ", u_s)
    print("********************************** U_V: ", u_v)

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    while True:
        _, frame = cap.read()

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        l_b = np.array([l_h, l_s, l_v])
        u_b = np.array([u_h, u_s, u_v])

        mask = cv2.inRange(hsv, l_b, u_b)

        res = cv2.bitwise_and(frame, frame, mask=mask)

        # Convert the processed frame to base64 encoding
        _, buffer = cv2.imencode('.jpg', res)
        res_base64 = base64.b64encode(buffer)

        return res_base64.decode('utf-8')
