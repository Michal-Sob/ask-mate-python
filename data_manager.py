import connection
from datetime import datetime
from operator import itemgetter

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


def max_id(data_base):
    lists_starts_with_0 = -1
    return len(data_base) + lists_starts_with_0


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
    for iterator in range(len(questions)):
        if questions[iterator]['id'] == str(question_id):
            del questions[iterator]
            break
    connection.export_updated_data(QUESTIONS_FILE_PATH, ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image'], questions)