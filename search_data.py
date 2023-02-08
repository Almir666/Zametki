def search_by_id():
    id = input("Введите ID для поиска: ")
    with open("data.txt", 'r') as file:
        data_text = file.readlines()
        if len(data_text) > 0:
            for item in data_text:
                if ("id: " + id + "; ") in item:
                    print(item)
        file.close()
def search_by_date():
    date = input("Введите дату и время для поиска: ")
    with open("data.txt", 'r') as file:
        data_text = file.readlines()
        if len(data_text) > 0:
            for item in data_text:
                if ("дата: " + date + "; ") in item:
                    print(item)
        file.close()
def search_by_header():
    head = input("Введите заголовок для поиска: ")
    with open("data.txt", 'r') as file:
        data_text = file.readlines()
        if len(data_text) > 0:
            for item in data_text:
                if ("заголовок: " + head + "; ") in item:
                    print(item)
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
                    print("not found")
                    return
        file.close()
def search_by():
    print("Параметры поиска:\n 1 - ID \n 2 - Дата \n 3 - По заголовку\n 4 - По слову \n 0 - выход \n")
    com = int(input())
    if com == 1:
        search_by_id()
    elif com == 2:
        search_by_date()
    elif com == 3:
        search_by_header()
    elif com == 4:
        search_by_word()
    elif com == 0:
        return
    print()