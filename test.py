import cv2
import urllib.request 
import numpy as np
from flask import Flask, render_template, Response


app = Flask(__name__,template_folder="C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python39")

def stream(ip):
    stream = urllib.request.urlopen("http://"+ ip + ":5010/api/v1/videostream/face")
    bytess = bytes('','utf-8')
    while True:
        bytess += stream.read(1024)
        a = bytess.find(b'\xff\xd8')
        b = bytess.find(b'\xff\xd9')
        if a != -1 and b != -1:
            jpg = bytess[a:b+2]
            bytess = bytess[b+2:]
            i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
            j = cv2.imencode('.jpeg',i)[1]
            frameSecond = j.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frameSecond + b'\r\n') # concat frame one by one and show result


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/video_feed')
def video_feed():
    return Response(stream('172.16.216.115',), mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/secondStream')
def secondStream():
    return Response(stream('172.16.216.116'), mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/thirdStream')
def thirdStream():
    return Response(stream('172.16.216.117'), mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/fourthStream')
def fourthStream():
    return Response(stream('172.16.216.118'), mimetype='multipart/x-mixed-replace; boundary=frame')

    
if __name__ == "__main__":
    app.run(debug=False)
