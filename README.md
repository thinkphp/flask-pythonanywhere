# flask

http://thinkphp.pythonanywhere.com/

from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Frank Sinatra"
