"""
Program: OpenCV Identify Numbers
Author: Hirushiharan Thevendran
Created On: 01.02.2024
Last Modified On: 06.02.2024

Programe Description: Python application using the OpenCV library to identify numbers in a video stream.
File Description: Flask application to for API functions.

Python Version: 3.10
"""

from flask import Flask, render_template, request, jsonify
from detect import identify_num
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/identify_numbers', methods=['POST'])
def start_opencv():
    lh_value = int(request.form['lhValue'])
    ls_value = int(request.form['lsValue'])
    lv_value = int(request.form['lvValue'])
    uh_value = int(request.form['uhValue'])
    us_value = int(request.form['usValue'])
    uv_value = int(request.form['uvValue'])

    try:
        res = identify_num(lh_value, ls_value, lv_value,
                           uh_value, us_value, uv_value)

        return jsonify({"results": res})

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == '__main__':
    app.run(debug=True)
