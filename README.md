# flask

http://thinkphp.pythonanywhere.com/

```Python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Frank Sinatra"
```    


export FLASK_APP=app.py

echo $FLASK_APP

flask run --host=0.0.0.0
