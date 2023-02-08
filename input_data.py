def inputData():
    id = input("ID заметки: ")
    date = input("Дата создания: ")
    header = input("Введите заголовок: ")
    text = input("Введите текст заметки: ")

    return [id, date, header, text]
