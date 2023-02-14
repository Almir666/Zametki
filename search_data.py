import csv
def search_by():
    key = input("Введите ключевое слово для поиска: ")
    with open("data.csv", 'r') as file:
        data_text = csv.reader(file)
        if len(str(data_text)) > 0:
            for item in data_text:
                for word in item:
                    if key in word:
                        print(item, "\n")
                        return
        else:
            print("Никаких заметок нет")
        file.close()
