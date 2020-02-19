import csv
QUESTIONS_FILE_PATH = 'sample_data/question.csv'


def import_data(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        return [dict(row) for row in reader]


def export_data(question):
    with open(QUESTIONS_FILE_PATH, 'a', newline='') as csvfile:
        fieldnames = ['id', 'submission_time', 'view_number', 'vote_number',
                      'title', 'message', 'image']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        return writer.writerow(question)