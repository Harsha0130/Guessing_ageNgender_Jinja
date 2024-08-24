from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route("/")
def home():
    ran_num = random.randint(1, 100)
    current_year = datetime.datetime.now().year
    return render_template("index.html", num=ran_num, year=current_year)


@app.route("/guess/<name>")
def guess(name):
    gender_api = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_api)
    gender = gender_response.json()["gender"]

    age_api = f"https://api.agify.io?name={name}"
    age_response = requests.get(age_api)
    age = age_response.json()["age"]
    return render_template("guess.html", my_name=name, gender=gender, age=age)


if __name__ == "__main__":
    app.run(debug=True)
