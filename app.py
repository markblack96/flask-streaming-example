from flask import Flask, render_template, Response

app = Flask(__name__)

# routes
@app.route('/')
def index():
    return render_template("index.html")

def gen():
    with open("static/long_ad.mp3", "rb") as ad:
        data = ad.read(1024)
        while data:
            yield data
            data = ad.read(1024)

@app.route('/audio-feed')
def audio_feed():
    return Response(gen(), mimetype="")