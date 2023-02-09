from write_file import write_data
from read_file import readF
from search_data import search_by
from del_data import del_by
from edit import edit_note

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
        edit_note()
    elif com == 5:
        del_by()
    elif com == 0:
        break


# id: 1; дата: 08.02.2023 21:49; заголовок: note 1; содержание: random text;
# id: 2; дата: 08.02.2023 21:50; заголовок: note 2; содержание: test data;
# id: 3; дата: 08.02.2023 21:51; заголовок: note 3; содержание: dg brgb nyjnyjmyjm ;
# id: 4; дата: 08.02.2023 21:55; заголовок: note 4; содержание: can i exit?;