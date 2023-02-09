def input_new_data():
    id = input("новое ID заметки: ")
    date = input("дата и время изменения: ")
    header = input("новый заголовок: ")
    text = input("новый текст: ")

    return [id, date, header, text]
def edit_note():
    dictionary = {}
    id = input("Введите ID заметки которую хотите отредактировать: ")
    with open("data.txt") as file:
        data_text = file.readlines()
        if len(data_text) > 0:
            for item in data_text:
                if ("id: " + id + "; ") in item:
                    print(item)
        else:
            print("Никаких заметок нет")
    new_data = input_new_data()
    with open("data.txt", "w") as f:
        for item in data_text:
            if ("id: " + id + "; ") in item:
                f.write("id: " + new_data[0] + "; ")
                f.write("дата: " + new_data[1] + "; ")
                f.write("заголовок: " + new_data[2] + "; ")
                f.write("содержание: " + new_data[3] + "; \n")
        for item in data_text:
            if ("id: " + id + "; ") not in item:
                f.write(item)
    file.close()

