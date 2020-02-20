import csv
QUESTIONS_FILE_PATH = 'sample_data/question.csv'
ANSWERS_FILE_PATH = 'sample_data/answer.csv'

def import_data(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        return [dict(row) for row in reader]


def export_data(data_base_path, fieldnames, new_row):
    with open(data_base_path, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        return writer.writerow(new_row)


def export_updated_data(data_base_path, fieldnames, new_questions):
    with open(data_base_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for line in new_questions:
            writer.writerow(line)
