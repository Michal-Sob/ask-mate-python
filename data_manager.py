import connection


QUESTIONS_FILE_PATH = 'sample_data/question.csv'
QUESTIONS = connection.import_data(QUESTIONS_FILE_PATH)