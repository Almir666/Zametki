from input_data import inputData
from write_file import write_data
from  read_file import readF
from search_data import search_by
# def createNote():

while True:
    print("Выберите команду: \n 1 - создать  2 - показать всё  3 - поиск  4 - редактировать  5 - удалить  0 - выход")
    com = int(input())
    if com == 1:
        write_data()
    elif com == 2:
        readF()
    elif com == 3:
        search_by()
    elif com == 4:
        print("work")
    elif com == 5:
        print("work")
    elif com == 0:
        break


