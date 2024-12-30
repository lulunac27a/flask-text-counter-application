from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")  # index page
def homepage() -> str:  # home page
    return render_template(
        "index.html", characters=0, words=0, lines=0, text_content=""
    )  # return index page template


@app.template_filter("comma_separator")  # comma separator filter
def comma_separator_filter(
    number: int | float,
) -> str:  # get number with comma separator as thousands separator
    # print number with comma separator as thousands separator
    return f"{number:,}"


@app.route("/calculate_text_counter", methods=["POST"])
def calculate_text_counter() -> str:  # calculate text counter
    # text content from text box area
    text_content: str = request.form["text_content"]
    characters: int = len(text_content)  # number of characters
    words: int = len(text_content.split())  # number of words
    lines: int = len(text_content.split("\n"))  # number of lines
    return render_template(
        "index.html",
        characters=characters,
        words=words,
        lines=lines,
        text_content=text_content,
    )  # return template with updated character, word and line count


if __name__ == "__main__":
    app.run(port=8081, debug=True)  # run the app at port 8081
