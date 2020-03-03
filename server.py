from flask import Flask, render_template, redirect, request
import data_manager

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template("index.html")


@app.route('/list', methods=['GET'])
def question_list():
    questions = data_manager.get_questions()
    print(questions)
    # if request.method == 'GET':
    #     sorting_list = request.args[0]
    #     asc = request.args[1]
    #     print(sorting_list)
    #     print(asc)
    # if request.method == 'GET':
    #     print('lulz')
    #     sort_by = request.args.get('author')
    #     title = request.args.get('title')
    #     return find_books(author, title)
    # order_by = title&order_direction = desc
    # data = {'title': 'hello', 'data[]': ['hello', 'world']}
    # response = request.GET('/list', params=data)

    return render_template('question_list.html', questions=questions)


@app.route('/add-question', methods=['GET', 'POST'])
def add_question():
    if request.method == "POST":
        new_question = dict(request.form)
        question_id = data_manager.new_question_manager(new_question)
        return redirect(f'show-question/{question_id}')

    return render_template('add_question.html')


@app.route('/question/<int:question_id>')
def show_question(question_id):
    selected_question = data_manager.get_questions(question_id=question_id)
    answers = data_manager.get_answers(question_id=question_id)
    return render_template('show_question.html', question_id=question_id, selected_question=selected_question, answers=answers)


@app.route('/question/<int:question_id>/delete')
def deleting_question(question_id):
    data_manager.delete_question(question_id)
    return redirect('/list')


@app.route('/question/<int:question_id>/new-answer', methods=['GET', 'POST'])
def add_answer(question_id):
    if request.method == "POST":
        new_answer = dict(request.form)
        data_manager.new_answer_manager(new_answer, question_id)
        return redirect(f'/question/{question_id}')

    return render_template('add_answer.html', question_id=question_id)


@app.route('/question/<int:question_id>/delete')
def delete_answer(question_id):
    data_manager.delete_question(question_id)
    return redirect('/list')


if __name__ == "__main__":
    app.run(
        debug=True,
        port=5000
            )
