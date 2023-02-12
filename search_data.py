def search_by_id():
    id = input("Введите ID для поиска: ")
    with open("data.txt", 'r') as file:
        data_text = file.readlines()
        if len(data_text) > 0:
            for item in data_text:
                if ("id: " + id + "; ") in item:
                    print(item)
        else:
            print("Никаких заметок нет")
        file.close()
def search_by_date():
    date = input("Введите дату и время для поиска: ")
    with open("data.txt", 'r') as file:
        data_text = file.readlines()
        if len(data_text) > 0:
            for item in data_text:
                if ("создано: " + date + "; ") in item:
                    print(item)
        else:
            print("Никаких заметок нет")
        file.close()
def search_by_word():
    word = input("Введите ключевое слово для поиска: ")
    with open("data.txt", 'r') as file:
        data_text = file.readlines()
        if len(data_text) > 0:
            for item in data_text:
                if word in item:
                    print(item)
        else:
            print("Никаких заметок нет")
        file.close()
def search_by():
    print("Параметры поиска:\n 1 - По ключевому слову \n 2 - По дате \n 3 - По ID \n 0 - выход \n")
    com = input()
    if com == '1':
        search_by_word()
    elif com == '2':
        search_by_date()
    elif com == '3':
        search_by_id()
    elif com == '0':
        return