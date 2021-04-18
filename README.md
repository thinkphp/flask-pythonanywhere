# flask

http://thinkphp.pythonanywhere.com/

```Python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Frank Sinatra"
```    
