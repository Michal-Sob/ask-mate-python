import connection
from datetime import datetime

QUESTIONS_FILE_PATH = 'sample_data/question.csv'
QUESTIONS = connection.import_data(QUESTIONS_FILE_PATH)

def submisson_time():
    now = datetime.now()
    timestamp = round(datetime.timestamp(now))

    return timestamp
