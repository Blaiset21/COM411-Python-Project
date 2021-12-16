import matplotlib.pyplot as plt
import csv


def read_data():
    with open('titanic.csv') as file:
        csv_reader = csv.reader(file)

        headings = next(csv_reader)
        data = {'survived': [], 'sex': [], 'age': [], 'fare': []}

        for values in csv_reader:
            data['survived'].append(values[1]).strip
            data['sex'].append(values[14]).strip
            data['age'].append(values[4]).strip
            data['fare'].append(values[8]).strip

            if ('survived' != "" and 'sex' != "" and 'age' != "" and 'fare' != ""):
                data['survived'].append(bool(int(survived)))

    return data