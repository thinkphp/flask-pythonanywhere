# flask

http://thinkphp.pythonanywhere.com/

```Python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Frank Sinatra"
```    

## Run Flask app as 0.0.0.0

export FLASK_APP=app.py

echo $FLASK_APP

flask run --host=0.0.0.0


## Template

from flask import Flask, render_template


```python
app = Flask(__name__)

@app.route("/")
def index():
    pagetitle = "HomePage"
    return render_template("index.html",
                            mytitle=pagetitle,
                            mycontent="Hello World")
```                            

```
myproject/
    /app/
        /templates/
            /index.html
        /views.py
        
index.html
```

```html
<html>
    <head>
        <title>{{ mytitle }}</title>
    </head>
    <body>
        <p>{{ mycontent }}</p>
    </body>
</html>
```
