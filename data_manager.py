import connection
from datetime import datetime
from operator import itemgetter


@connection.connection_handler
def get_answers(cursor, question_id):
    cursor.execute("""SELECT * FROM answer WHERE question_id = (%s)""", (question_id,))
    answers = [dict(row) for row in cursor.fetchall()]
    return answers


@connection.connection_handler
def get_questions(cursor, question_id=None):
    if not question_id:
        cursor.execute("""SELECT * FROM question """)
        questions = [dict(row) for row in cursor.fetchall()]
    else:
        cursor.execute("""SELECT * FROM question WHERE id = (%s)""", (question_id,))
        questions = [dict(row) for row in cursor.fetchall()]
    return questions


def connect_question_with_his_answer(id):
    selected_question = [question for question in get_questions() if question['id'] == id]
    for answer in get_answers():
        if id == answer['question_id']:
            selected_question.append(answer)
    return selected_question


def new_question_data():
    new_id = max_id(get_questions()) + 1
    data = {
        "id": str(new_id),
        "submission_time": str(submission_time()),
        "view_number": "0",
        "vote_number": "0"
    }
    return data


def new_question_manager(new_question):
    new_question.update(new_question_data())
    fieldnames = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']
    connection.export_data(QUESTIONS_FILE_PATH, fieldnames, new_question)

    new_question_id = max_id(get_questions())

    return new_question_id


@connection.connection_handler
def new_question_manager(cursor, new_question):
    cursor.execute("""INSERT INTO question (title,submission_time, message) VALUES (%s,%s,%s);""", (new_question['title'], util.submission_time(), new_question['message'],))
    cursor.execute("""SELECT id FROM question WHERE title= %(title)s;""", {'title': new_question['title'], 'message': new_question['message']})
    question_id = dict(cursor.fetchone())['id']
    return question_id


def new_answer_data(question_id):
    new_id = max_id((get_answers())) + 1
    data = {
        "id": str(new_id),
        "submission_time": str(submission_time()),
        "vote_number": "0",
        "question_id": str(question_id)
    }
    return data


def new_answer_manager(new_answer, question_id):
    new_answer.update(new_answer_data(question_id))
    fieldnames = ['id', 'submission_time', 'vote_number', 'question_id', 'message', 'image']
    connection.export_data(ANSWERS_FILE_PATH, fieldnames, new_answer)
    return None


def sorting_questions(sorting_list, reversing):
    sorted(get_questions(), key=itemgetter(sorting_list), reverse=reversing)


def delete_question(question_id):
    questions = connection.import_data(QUESTIONS_FILE_PATH)
    answers = connection.import_data(ANSWERS_FILE_PATH)
    for iterator in range(len(questions)):
        if questions[iterator]['id'] == str(question_id):
            del questions[iterator]
            break
    for answer in answers[:]:
        if answer['question_id'] == str(question_id):
            del answers[answers.index(answer)]

    connection.export_updated_data(QUESTIONS_FILE_PATH, ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image'], questions)
    connection.export_updated_data(ANSWERS_FILE_PATH, ['id', 'submission_time', 'vote_number', 'question_id', 'message', 'image'], answers)


@connection.connection_handler
def delete_question(cursor):
    questions = get_questions(cursor)
    answers = get_answers(cursor)
    for iterator in range(len(questions)):
        if questions[iterator]['id'] == str(question_id):
            del questions[iterator]
            break
    for answer in answers[:]:
        if answer['question_id'] == str(question_id):
            del answers[answers.index(answer)]