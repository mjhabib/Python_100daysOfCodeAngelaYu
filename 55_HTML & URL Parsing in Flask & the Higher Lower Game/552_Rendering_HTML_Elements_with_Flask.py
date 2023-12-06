from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return ('<h1 style="text-align:center" > Hello homepage ...</h1>'
            '<p>This is a paragraph</p>')
