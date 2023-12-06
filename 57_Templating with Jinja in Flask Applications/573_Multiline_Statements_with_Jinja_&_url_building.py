from flask import Flask, render_template
import requests

app = Flask(__name__)

blog_posts = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(blog_posts)
all_posts = response.json()


@app.route("/")
def blog():
    return render_template("573_index.html", posts=all_posts)


# url building + passing any parameters from html file to here
@app.route("/blogs/<number>")
def all_blogs(number):
    print(number)  # just to test that it works
    return render_template("573_index_blogs.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
