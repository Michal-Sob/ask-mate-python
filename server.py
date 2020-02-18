from flask import Flask, render_template, redirect, request
import data_manager


app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template("index.html")


@app.route('/list')
def question_list():
    questions = data_manager.QUESTIONS
    return render_template('question_list.html', questions=questions)


@app.route('/add-question', methods=['GET', 'POST'])
def add_question():
    return render_template('add_question.html')


if __name__ == "__main__":
    app.run(
        debug=True,
        port=5000
            )