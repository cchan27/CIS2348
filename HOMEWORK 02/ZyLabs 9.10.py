# Caleb Chan, 1831296
import csv
filename = input()
with open(filename, 'r') as file:
    word_reader = csv.reader(file, delimiter=',')
    result = dict()
    for word in word_reader:
        for number in word:
            if number in result:
                result[number] += 1
            else:
                result[number] = 1
        for k in list(result.keys()):
            print('{} {}'.format(k, result[k]))
