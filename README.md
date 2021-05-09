# flask

http://thinkphp.pythonanywhere.com/

- python3 -V
- sudo apt install python3-venv
- mkdir flask_app && cd flask_app
- python3 -m venv venv
- source venv/bin/activate
- (venv) $ pip install Flask
- (venv) $ python -m flask --version
- (venv) $ pip freeze
- (venv) $ export FLASK_APP=hello.py
- (venv) $ echo $FLASK_APP
- (venv) $ hello.py # ok
- (venv) $ flask run --host=0.0.0.0 --port=5000 #run in container


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

flask run --host=0.0.0.0 0 --port=3000
    


## Template

```
from flask import Flask, render_template

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

Reference
- https://linuxize.com/post/how-to-install-flask-on-ubuntu-20-04/
- https://flask.palletsprojects.com/en/1.1.x/quickstart/
- https://testdriven.io/blog/combine-flask-vue/
