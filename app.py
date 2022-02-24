from flask import Flask, render_template
from flask.wrappers import Response
from camera import Video
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('main.html')

def gen(camera):
    while True:
        frame=camera.get_frame()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame +
               b'\r\n\r\n')

@app.route('/video')
def video():
    return Response(gen(Video()),
    mimetype='multipart/x-mixed-replace; boundary=frame')


app.run(debug=True)