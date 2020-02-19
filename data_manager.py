import connection
from datetime import datetime

QUESTIONS_FILE_PATH = 'sample_data/question.csv'
ANSWERS_FILE_PATH = 'sample_data/answer.csv'


def get_answers():
    global ANSWERS_FILE_PATH
    return connection.import_data(ANSWERS_FILE_PATH)


def get_questions():
    global QUESTIONS_FILE_PATH
    return connection.import_data(QUESTIONS_FILE_PATH)


def connect_question_with_his_answer(id):
    selected_question = [question for question in get_questions() if question['id'] == id]
    for answer in get_answers():
        if id == answer['question_id']:
            selected_question.append(answer)
    return selected_question


def submission_time():
    now = datetime.now()
    timestamp = round(datetime.timestamp(now))

    return timestamp


def max_id():
    lists_starts_with_0 = -1
    return len(get_questions()) + lists_starts_with_0


def new_question_data():
    new_id = max_id() + 1
    data = {
        "id": str(new_id),
        "submission_time": str(submission_time()),
        "view_number": "0",
        "vote_number": "0"
    }
    return data


def new_question_manager(new_question):
    new_question.update(new_question_data())

    connection.export_data(new_question)

    new_question_id = max_id() + 1

    return new_question_id