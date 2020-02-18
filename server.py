from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def main_page():
    return "<h1>Będzie dobrze Panowie<h1>"


if __name__ == "__main__":
    app.run(
        debug=True,
        port=5000
            )