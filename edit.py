def edit_head():
    id = input("Введите ID заметки которую хотите отредактировать: ")
    with open("data.txt", 'r') as file:
        data_text = file.readlines()
        if len(data_text) > 0:
            for item in data_text:
                if ("id: " + id + "; ") in item:
                    print(item)
        else:
            print("Никаких заметок нет")
        file.close()

    print("Запишите новый текст: ")
    new_data = input()

def edit_text():
    print("working...")

def edit_note():
    print("Редактировать: \n 1 - Заголовок \n 2 - Содержание \n 0 - выход \n")
    com = int(input())
    if com == 1:
        edit_head()
    elif com == 2:
        edit_text()
    elif com == 0:
        return