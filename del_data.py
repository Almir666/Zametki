def delete_row():
    print("Укажите номер строки: ")
    with open("data.txt") as file:
        id_del = int(input())
        id_note = file.readlines()
        del id_note[id_del - 1]
        with open("data.txt", "w") as f:
            for item in id_note:
                f.write(item)
        file.close()
def delete_by_id():
    print("Заметку можно удалить по ID")
    with open("data.txt") as file:
        id_del = input()
        id_note = file.readlines()

    with open("data.txt", "w") as f:
        for item in id_note:
            if ("id: " + id_del + "; ") not in item:
                f.write(item)
        file.close()
def del_by():
    print("Удалить заметку можно по ID или номеру строки: \n 1 - ID \n 2 - № строки \n 0 - выход \n")
    com = input()
    if com == '1':
        delete_by_id()
    elif com == '2':
        delete_row()
    elif com == '0':
        return
    else:
        print("нужно ввести цифру от 0 до 2")