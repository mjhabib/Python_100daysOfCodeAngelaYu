from flask import Flask
app = Flask(__name__)  # '__name__' is one of the built-in special attributes in python


@app.route('/')
# this is a 'function decorator' which runs the below function only when we goto to the 'root address' as defined
def hello_world():
    return 'Hello World!'


@app.route('/bye')
def say_bye():
    return "Bye ..."


if __name__ == '__main__':
    # basically we're telling the compiler where the current app code is located to run it which is here not in another file
    app.run()
