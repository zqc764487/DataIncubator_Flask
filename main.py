from flask import Flask, render_template, request
import os

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    return render_template("upload.html")

@app.route("/upload", methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'static/')

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        #filename = file.filename
        destination = "/".join([target, "temp.jpg"])
        print(destination)
        file.save(destination)
    return render_template("complete.html")

