from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("index.html", characters=0, words=0, lines=0)


@app.route("/calculate_text_counter", methods=["POST"])
def calculate_text_counter():
    text_content = request.form["text_content"]
    characters = len(text_content)
    words = len(text_content.split())
    lines = len(text_content.split("\n"))
    return render_template(
        "index.html", characters=characters, words=words, lines=lines
    )
