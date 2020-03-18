from flask import Flask, render_template, redirect, request, url_for, session, escape
import data_manager, util

app = Flask(__name__)

app.secret_key = b'_5#y2Lk7\n\udp'


@app.route('/')
def main_page():
    questions = data_manager.get_questions()
    return render_template("index.html", questions=questions, logged_in=util.is_logged_in())


@app.route('/list/<search>', methods=['GET'])
@app.route('/list', methods=['GET'])
def question_list(search=None):
    text = None
    if search:
        text = request.args.get('text')
        questions = data_manager.search_by_title_or_message(text)
    else:
        questions = data_manager.get_questions()
    return render_template('question_list.html', questions=questions, text=text, logged_in=util.is_logged_in())


@app.route('/question/<int:question_id>/update', methods=['GET', 'POST'])
@app.route('/add-question', methods=['GET', 'POST'])
def add_question(question_id=None):
    if not util.is_logged_in():
        return redirect('/login')
    if request.method == "POST":
        new_question = dict(request.form)
        if question_id:
            question_id = data_manager.update_question(question_id, new_question, session['email'])
        else:
            question_id = data_manager.new_question_manager(new_question, session['email'])
        return redirect(f'/question/{question_id}')

    selected_question = None
    if question_id:
        selected_question = data_manager.get_questions(question_id=question_id)[0]

    return render_template('add_question.html', selected_question=selected_question, question_id=question_id,
                           logged_in=util.is_logged_in())


@app.route('/question/<int:question_id>')
def show_question(question_id):
    selected_question = data_manager.get_questions(question_id=question_id)[0]
    answers = data_manager.get_answers(question_id=question_id)
    question_comments = data_manager.get_comments(question_id)

    try:
        answer_id = answers[0]['id']
    except IndexError:
        answer_id = None

    comments = data_manager.get_comments(question_id=question_id)
    # answers_comments = None
    return render_template('show_question.html', question_id=question_id, selected_question=selected_question, answers=answers,
                           answer_id=answer_id, comments=comments, logged_in=util.is_logged_in())


@app.route('/question/<int:question_id>/delete')
def deleting_question(question_id):
    if util.is_logged_in() and session['email'] == data_manager.get_user_email(question_id, 'question'):
        data_manager.delete_question(question_id)
    else:
        return redirect(url_for('log_in'))
    return redirect('/list')


@app.route('/answer/<int:answer_id>/update', methods=['GET', 'POST'])
@app.route('/question/<int:question_id>/new-answer', methods=['GET', 'POST'])
def add_answer(question_id=None, answer_id=None):
    answers = data_manager.get_answers()
    message = None
    if not util.is_logged_in():
        return redirect('/login')
    if request.method == "POST":
        new_answer = dict(request.form)
        if answer_id and session['email'] == data_manager.get_user_email(answer_id, 'answer'):
            question_id = data_manager.update_answer(answer_id, new_answer)['question_id']
        else:
            new_answer['question_id'] = question_id
            new_answer['user_email'] = session['email']
            question_id = data_manager.new_answer_manager(new_answer)
        return redirect(f'/question/{question_id}')
    if answer_id:
        for answer in answers:
            if answer['id'] == answer_id:
                question_id = answer['question_id']
                message = answer['message']

    return render_template('add_answer.html', question_id=question_id, answer_id=answer_id, message=message,
                           logged_in=util.is_logged_in())


@app.route('/answer/<int:answer_id>/delete')
def delete_answer(answer_id):
    question_id = None
    answers = data_manager.get_answers()
    for answer in answers:
        if answer['id'] == answer_id:
            question_id = answer['question_id']
    data_manager.delete_answer(answer_id)
    return redirect(url_for('show_question', question_id=question_id), logged_in=util.is_logged_in())


@app.route('/question/<int:question_id>/new-comment', methods=['GET', 'POST'])
def add_question_comment(question_id):
    if request.method == "POST":
        new_comment = dict(request.form)
        new_comment['question_id'] = question_id
        data_manager.new_comment_manager(new_comment)

        return redirect(f'/question/{question_id}')

    return render_template('add_comment.html', question_id=question_id, logged_in=util.is_logged_in())


# Work in progress
@app.route('/answer/<int:answer_id>/new-comment', methods=['GET', 'POST'])
def add_answer_comment(answer_id):
    if request.method == "POST":
        new_comment = dict(request.form)
        new_comment['answer_id'] = answer_id
        data_manager.new_comment_manager(new_comment)

        return redirect(f'/question/{question_id}')

    return render_template('add_comment.html', answer_id=answer_id, logged_in=util.is_logged_in())
# Work in progress


@app.route('/contact')
def contact():
    return render_template('contact.html', logged_in=util.is_logged_in())


@app.route('/login', methods=["GET", "POST"])
def log_in():
    wrong_data = None
    if request.method == "POST":
        session['email'] = request.form['email']
        if util.verify_password(request.form['password'], data_manager.get_user_password_by_email(session['email'])):
            return redirect('/')
        else:
            session.pop('email', None)
            wrong_data = 'Invalid user name or password  '
            return render_template('login.html', logged_in=util.is_logged_in(), wrong_data=wrong_data)
    return render_template('login.html', logged_in=util.is_logged_in(), wrong_data=wrong_data)


@app.route('/logout')
def log_out():
    session.pop('email', None)
    return redirect(url_for('main_page'))


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':

        new_user = dict(request.form)

        data_manager.add_user(new_user)

        return redirect(url_for('main_page'))

    return render_template('registration_form.html')


if __name__ == "__main__":
    app.run(
        debug=True,
        port=5000
    )
