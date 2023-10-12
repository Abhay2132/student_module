from flask import Flask , render_template, request, flash, redirect
from werkzeug.utils import secure_filename
from pathlib import Path
import os
import hlpr

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

@app.route("/upload", methods=["post"])
def _upload():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    print("file : ", file)
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('download_file', name=filename))