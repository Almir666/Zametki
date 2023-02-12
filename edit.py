import datetime
def input_new_data():
    header = input("новый заголовок: ")
    text = input("новый текст: ")

    return [header, text]
def edit_note():
    id = input(" Заметку можно найти по ID \n Выйти - 0 \n")
    if len(str(id)) <= 3 and id.isdigit():
        if id != '0':
            with open("data.txt") as file:
                data_text = file.readlines()
                if len(data_text) > 0:
                    for item in data_text:
                        if ("id: " + id + "; ") in item:
                            print(item)
                else:
                    print("Никаких заметок нет")
            date = datetime.datetime.today() - datetime.timedelta(1)
            new_data = input_new_data()
            with open("data.txt", "w") as f:
                for item in data_text:
                    if ("id: " + id + "; ") in item:
                        f.write('* ' + new_data[0] + ": ")
                        f.write(new_data[1] + "; ")
                        f.write("изменено: " + str(date.strftime('%Y-%m-%d %H:%M:%S')) + "; ")
                        f.write("id: " + id + "; \n")
                for item in data_text:
                    if ("id: " + id + "; ") not in item:
                        f.write(item)
            file.close()
        else:
            return
    else:
        print('нужно ввести идентификатор в виде цифры')
        return



