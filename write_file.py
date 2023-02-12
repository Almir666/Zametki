from input_data import inputData
import datetime
from random import randint
def write_data():
    date = datetime.datetime.today() - datetime.timedelta(1)
    id = randint(0,999)
    file = open('data.txt', 'a')
    data = inputData()
    file.write('* ' + data[0] + ": ")
    file.write('"' + data[1] + '"' + "; ")
    file.write("создано: " + str(date.strftime('%Y-%m-%d %H:%M:%S')) + "; ")
    file.write("id: " + str(id) + "; \n")
    file.close()
    print("Заметка создана!" + "\n")