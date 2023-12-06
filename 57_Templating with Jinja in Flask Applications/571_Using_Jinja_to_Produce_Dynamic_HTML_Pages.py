from flask import Flask, render_template
import random
import datetime as dt

app = Flask(__name__)


@app.route("/")
def home():
    ran_num = random.randint(1, 11)
    year = dt.datetime.now().year
    return render_template("571_index.html", num=ran_num, year=year)  # **kwargs


if __name__ == "__main__":
    app.run(debug=True)

