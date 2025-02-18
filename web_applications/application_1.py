from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    port = request.environ.get("SERVER_PORT")
    return render_template("index.html", port=port)


@app.route("/about")
def about():
    return "Application 1"


@app.errorhandler(404)
def page_not_found(error):
    return render_template("page_not_found.html"), 404


if __name__ == "__main__":
    app.run(port=8000)
