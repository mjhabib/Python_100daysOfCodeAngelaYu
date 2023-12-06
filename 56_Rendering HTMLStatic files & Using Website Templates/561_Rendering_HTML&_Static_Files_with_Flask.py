from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("561_mj_cv.html")
    # the html file must be inside a folder called 'templates'


if __name__ == "__main__":
    app.run(debug=True)
