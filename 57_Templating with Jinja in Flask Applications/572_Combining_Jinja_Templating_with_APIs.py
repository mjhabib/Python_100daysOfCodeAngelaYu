from flask import Flask, render_template
import requests

app = Flask(__name__)

AGE_ENDPOINT = "https://api.agify.io"
GENDER_ENDPOINT = "https://api.genderize.io"


def age_api(name):
    age_response = requests.get(f"{AGE_ENDPOINT}?name={name}")
    age_response.raise_for_status()
    age_result = age_response.json()
    return age_result["age"]


def gender_api(name):
    gender_response = requests.get(f"{GENDER_ENDPOINT}?name={name}")
    gender_response.raise_for_status()
    gender_result = gender_response.json()
    return gender_result["gender"]



@app.route("/")
def home():
    return render_template("572_index.html")


@app.route("/<url_name>")
def name_page(url_name):
    age = age_api(url_name)
    gender = gender_api(url_name)
    return render_template("572_index_name.html", name=url_name, gender=gender, age=age)


if __name__ == "__main__":
    app.run(debug=True)

