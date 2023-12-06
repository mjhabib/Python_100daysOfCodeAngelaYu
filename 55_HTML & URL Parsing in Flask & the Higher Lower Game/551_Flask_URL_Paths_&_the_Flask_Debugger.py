from flask import Flask

app = Flask(__name__)


@app.route("/")
def homepage():
    return "You are in the homepage ..."


@app.route("/username/<name>")  # to get a variable passed into the url and do st. with it
def say_hello_name(name):
    return f"Hello {name}"


@app.route("/username/<name>/<int:number>")
def say_hello_age(name, number):
    return f"Hello {name}, You are {number} years old"
# I can also use <path:name> if I want to print the entire path with slashes, etc...


if __name__ == "__main__":
    app.run()
    # app.run(debug=True)
    # this parameter was supposed to activate Flask debugger mode, but instead I have to activate it inside the configuration file for this project to work
    # debugger mode has another functionality which is auto-reload which means I don't have to re-run my program each time I've done a change
