from flask import Flask
import random

ran_number = random.randint(0, 9)
print(ran_number)


app = Flask(__name__)


@app.route("/")
def guess_number():
    return ("<h1>Guess a number between 0 and 9 and type it into the URL after home address</h1><br>"
            '<iframe src="https://giphy.com/embed/DhiRqIsofVMi7fWNBQ" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/IN10medianetwork-nakul-akul-asuras-DhiRqIsofVMi7fWNBQ">via GIPHY</a></p>')


@app.route("/<int:num_url>")
def user_input(num_url):
    if num_url == ran_number:
        return ('<h1 style="color:green">You are right :)</h1><br>'
                '<iframe src="https://giphy.com/embed/l4JySAWfMaY7w88sU" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/brooklynninenine-fox-brooklyn-nine-nine-l4JySAWfMaY7w88sU">via GIPHY</a></p>')

    elif num_url > ran_number:
        return ('<h1 style="color:red">Too high, try again!</h1><br>'
                '<iframe src="https://giphy.com/embed/iZGpuaRKdEZoI" width="480" height="464" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/movie-funny-up-iZGpuaRKdEZoI">via GIPHY</a></p>')

    elif num_url < ran_number:
        return ('<h1 style="color:blue">Too low, try again!</h1><br>'
                '<iframe src="https://giphy.com/embed/BaXZhPYWMJ1nWfbSk6" width="480" height="202" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/ImportWorx-BaXZhPYWMJ1nWfbSk6">via GIPHY</a></p>')


if __name__ == "__main__":
    app.run(debug=True)
