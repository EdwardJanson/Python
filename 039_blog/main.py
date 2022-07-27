from flask import Flask, render_template
import requests


app = Flask(__name__)


def blog_data():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return all_posts


@app.route('/')
def home():
    return render_template("index.html", posts=blog_data())


@app.route('/post/<num>')
def get_blog(num):
    return render_template("post.html", posts=blog_data(), blog_id=int(num))


if __name__ == "__main__":
    app.run(debug=True)
