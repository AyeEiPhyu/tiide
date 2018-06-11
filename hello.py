from flask import Flask

app = Flask(__name__)

@app.route("/")
def Aye():
    return "Hello World"

@app.route("/Aye")
def tiide():
    return "Welcome to Aye Ei Phyu"
