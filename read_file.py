def readF():
    file = open('data.txt')
    data = file.read()
    if len(data) > 0:
        print(data)
    else:
        print("Заметок нет \n")
    file.close()