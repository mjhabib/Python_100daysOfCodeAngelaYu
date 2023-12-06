from flask import Flask, render_template
import requests


app = Flask(__name__)

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
response.raise_for_status()
all_posts = response.json()


@app.route('/')
def home():
    return render_template("574_index.html", posts=all_posts)


@app.route("/post/<int:id>")
def posts(id):
    url_id = id
    return render_template("574_post.html", posts=all_posts,  post_id=url_id)


if __name__ == "__main__":
    app.run(debug=True)
