import connection
from datetime import datetime

QUESTIONS_FILE_PATH = 'sample_data/question.csv'
QUESTIONS = connection.import_data(QUESTIONS_FILE_PATH)


def submission_time():
    now = datetime.now()
    timestamp = round(datetime.timestamp(now))
    return timestamp


def max_id():
    lists_starts_with_0 = -1
    return len(QUESTIONS) + lists_starts_with_0


def new_question_data():
    new_id = max_id() + 1
    data = {
        "id": str(new_id),
        "submission_time": str(submission_time()),
        "view_number": "0",
        "vote_number": "0"
    }
    return data