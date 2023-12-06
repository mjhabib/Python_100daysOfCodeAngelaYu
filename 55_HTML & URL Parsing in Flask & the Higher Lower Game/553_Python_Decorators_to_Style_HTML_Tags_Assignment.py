from flask import Flask

app = Flask(__name__)


def bold_decorator(function):
    def wrapper_bold():
        return f"<b>{function()}</b>"

    return wrapper_bold


def underline_decorator(function):
    def wrapper_underline():
        return f"<u>{function()}</u>"

    return wrapper_underline


def italic_decorator(function):
    def wrapper_italic():
        return f"<em>{function()}</em>"

    return wrapper_italic


@app.route("/")
@bold_decorator
@italic_decorator
@underline_decorator
def a_new_text():
    return 'This is my text that I am going to decorate ...'


if __name__ == "__main__":
    app.run(debug=True)
