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


def submisson_time():
    now = datetime.now()
    timestamp = round(datetime.timestamp(now))

    return timestamp
