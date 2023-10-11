from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def login():
    return render_template('index.html')

@app.route("/gallery")
def panel():
    return render_template('gallery.html')

@app.route("/login", methods=["post"])
def _login():
    return "{ok:false}"