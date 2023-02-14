from write_file import write_data
from read_file import readF
from search_data import search_by
from del_data import delete_note
from edit import edit_note

while True:
    print("Выберите команду: \n 1 - создать  2 - показать всё  3 - поиск  4 - редактировать  5 - удалить  0 - выход")
    com = input()
    if com == '1':
        write_data()
    elif com == '2':
        readF()
    elif com == '3':
        search_by()
    elif com == '4':
        edit_note()
    elif com == '5':
        delete_note()
    elif com == '0':
        break
    else:
        print("Введите корректную цифру, от 0 до 5")
