import csv
from input_data import inputData
import datetime
from random import randint
def write_data():
    date = datetime.datetime.today() - datetime.timedelta(1)
    id = randint(1,99)
    file = open('data.csv', 'a')
    writer = csv.writer(file)
    data = inputData()
    writer.writerow(['* ' + data[0], data[1], "создано: " + str(date.strftime('%Y-%m-%d %H:%M:%S')), "id: " + str(id)])
    file.close()
    print("Заметка создана!" + "\n")