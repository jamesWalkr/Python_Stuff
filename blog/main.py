from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def home():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)


@app.route("/post/<blog_id>")
def get_blogs(blog_id):
    return "this is will be page to individual blog post"


if __name__ == "__main__":
    app.run(debug=True)
