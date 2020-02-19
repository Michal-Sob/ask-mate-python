from flask import Flask, render_template, redirect, request
import data_manager
import connection

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
        new_question.update(data_manager.new_question_data())
        print(new_question)
        connection.export_data(new_question)
        id_question = data_manager.max_id() + 1
        return redirect(f'show-question/{id_question}')

    return render_template('add_question.html')


@app.route('/show-question/<int:question_id>')
def show_question(question_id):
    picked_question = {}
    for question in data_manager.get_questions():
        if question_id == int(question['id']):
            picked_question = question
            print(picked_question)
    return render_template('show_question.html', picked_question=picked_question)





if __name__ == "__main__":
    app.run(
        debug=True,
        port=5000
            )