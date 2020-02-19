from flask import Flask, render_template, redirect, request
import data_manager


app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template("index.html")


@app.route('/list')
def question_list():
    questions = data_manager.get_questions()
    return render_template('question_list.html', questions=questions)


@app.route('/add-question', methods=['GET', 'POST'])
def add_question():
    if request.method == "POST":
        new_question = dict(request.form)
        print(new_question)
        return neww

        # title = dict(request.form('title'))
    return render_template('add_question.html')


@app.route('/show-question/<int:question_id>')
def show_question(question_id):
    selected_question = data_manager.connect_question_with_his_answer(str(question_id))
    return render_template('show_question.html', selected_question=selected_question)


if __name__ == "__main__":
    app.run(
        debug=True,
        port=5000
            )