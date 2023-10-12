import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from pathlib import Path

Path("uploads").mkdir(exist_ok=True)
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 2 * 1000 * 1000