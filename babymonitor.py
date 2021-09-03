from flask import Flask, render_template, Response, request
from camera import VideoCamera
from temperature import TemperatureProbe
from audio import Microphone
import pyaudio
from datetime import datetime

# create the camera, temp and microphone
camera = VideoCamera() 
temp_probe = TemperatureProbe()
microphone = Microphone()

app = Flask(__name__)

# return index.html from templates
@app.route('/')
def index():
    return render_template('index.html')

# get the video frames for index.html
@app.route('/video_feed')
def video_feed():
    return Response(gen_cam(camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# get the time for index.html
@app.route('/time_feed')
def time_feed():
    return Response(gen_time(), mimetype='text')

# get a temperature for index.html
@app.route('/temp_feed')
def temp_feed():
    return Response(gen_temp(temp_probe), mimetype='text')

# get an audio chunk for index.html
@app.route('/audio_feed')
def audio_feed():
    return Response(gen_audio(microphone), mimetype='audio/x-wav')

# always get the next frame from the camera
def gen_cam(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

# get the time when requested. set to 1000ms in html.index
def gen_time():
    yield datetime.now().strftime("%H:%M:%S<br>%d.%m.%Y")

# get the temperature when requested. set to 1000ms in html.index
def gen_temp(temp_probe):
    yield temp_probe.read_temp()

# always get the next chunk of audio
def gen_audio(microphone):
    data = microphone.get_wav_header()
    first_chunk = True
    # if it is the first chunk add a header to it.
    while True:
        if first_chunk:
            data += microphone.get_audio()
            first_chunk = False
        else:
            data = microphone.get_audio()
        yield (data)

# run the flask app automatically
if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=False)
    


