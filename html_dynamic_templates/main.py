from flask import Flask, render_template
from datetime import date
import requests

app = Flask(__name__)


@app.route("/")
def home():
    curr_year = date.today().year
    return render_template("index.html", year=curr_year)


@app.route("/guess/<name>")
def gusess(name):
    gender_url = f"https://api.genderize.io/?name={name}"
    response_gender = requests.get(gender_url)
    response_gender.raise_for_status
    gender_data = response_gender.json()
    api_gender = gender_data["gender"]

    age_url = f"https://api.agify.io/?name={name}"
    response_age = requests.get(age_url)
    response_age.raise_for_status
    age_data = response_age.json()
    api_name = age_data["name"]
    api_age = age_data["age"]

    return render_template(
        "guess.html", name=api_name.title(), age=api_age, gender=api_gender
    )


@app.route("/blog")
def get_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()

    return render_template("blog.html", posts=all_posts)


if __name__ == "__name__":
    app.run(debug=True)
