import csv
def delete_note():
    key = input("Введите ID заметки что бы выбрать её: ")
    new_data = []
    count = 0
    file = open("data.csv", 'r')
    data_text = csv.reader(file)
    for item in data_text:
        new_data.append(item)
        if ("id: " + key) in item:
            count +=1
            print(item)
    if count == 0:
        print("Ничего не найдено\n")
        return
    file.close()
    com = input("Удалить заметку? - y/n \n")
    if com == 'y' or com == 'Y':
        f = open("data.csv", 'w')
        writer = csv.writer(f)
        for item in new_data:
            if ("id: " + key) not in item:
                writer.writerow(item)
        print("Заметка удалена")
        f.close()
    elif com == 'n' or com == 'N':
        return
    else:
        print("Не корректная команда")
