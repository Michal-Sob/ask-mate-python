import csv


def import_data(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        return [dict(row) for row in reader]