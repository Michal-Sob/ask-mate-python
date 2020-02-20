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
        question_id = data_manager.new_question_manager(new_question)
        return redirect(f'show-question/{question_id}')

    return render_template('add_question.html')


@app.route('/show-question/<int:question_id>')
def show_question(question_id):
    selected_question = data_manager.connect_question_with_his_answer(str(question_id))
    return render_template('show_question.html', selected_question=selected_question, leng=len(selected_question))


@app.route('/question/<int:question_id>/delete')
def deleting_question(question_id):
    pass


@app.route('/show-question/<int:question_id>/new-answer', methods=['GET', 'POST'])
def add_answer(question_id):
    if request.method == "POST":
        print(question_id)
        new_answer = dict(request.form)
        data_manager.new_answer_manager(new_answer, question_id)
        return redirect(f'/show-question/{question_id}')

    return render_template('add_answer.html', question_id=question_id)


@app.route('show-question/<int:question_id/delete')
def delete_answer(question_id):
    data_manager.delete_question(question_id)
    return redirect('/list')


if __name__ == "__main__":
    app.run(
        debug=True,
        port=5000
            )