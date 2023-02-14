import datetime
import csv
def input_new_data():
    header = input("новый заголовок: ")
    text = input("новый текст: ")
    return [header, text]

def edit_note():
    date = datetime.datetime.today() - datetime.timedelta(1)
    id = input(" Заметку можно найти по ID \n Выйти - 0 \n")
    if len(str(id)) <= 3 and id.isdigit():
        if id != '0':
            new_data = []
            file = open("data.csv", 'r')
            data_text = csv.reader(file)
            for item in data_text:
                new_data.append(item)
                if ("id: " + id) in item:
                    print(item)
            file.close()
            new_text = input_new_data()
            f = open("data.csv", 'w')
            writer = csv.writer(f)
            writer.writerow(['* ' + new_text[0], new_text[1], "изменено: " + str(date.strftime('%Y-%m-%d %H:%M:%S')),
                             "id: " + str(id)])
            for item in new_data:
                if ("id: " + id) not in item:
                    writer.writerow(item)
            f.close()
            print("изменения сохранены")
        else:
            return
    else:
        print('нужно ввести идентификатор в виде цифры')
        return


