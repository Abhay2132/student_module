from flask import Flask , render_template, request, flash, redirect
from pathlib import Path
import os
from hlpr import saveImg

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
Path(UPLOAD_FOLDER).mkdir(exist_ok=True)

print("__name__ : " ,__name__)
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 2 * 1000 * 1000
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

@app.route("/")
def login():
    return render_template('index.html')

@app.route("/gallery")
def panel():
    return render_template('gallery.html')

@app.route("/upload")
def upload():
    return render_template('upload.html')

@app.route("/login", methods=["post"])
def _login():
    return "{ok:false}"

@app.route("/_upload", methods=["post"])
def _upload():
    fieldName = 'imgs'
    print("/upload")
    if fieldName not in request.files:
        print("error : no file in body")
        return "{error : 'no file in body'}"
    files = request.files.getlist(fieldName)
    # print("files", request.files.getlist(fieldName))
    
    lastRes = {}
    for file in files :
        lastRes = saveImg(file, UPLOAD_FOLDER=app.config['UPLOAD_FOLDER'])
        if 'error' in lastRes.keys() : 
            return lastRes["error"]
    
    return lastRes['status']