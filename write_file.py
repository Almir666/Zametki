from input_data import inputData

def write_data():
    file = open('data.txt', 'a')
    data = inputData()
    file.write("id: " + data[0] + "; ")
    file.write("дата: " + data[1] + "; ")
    file.write("заголовок: " + data[2] + "; ")
    file.write("содержание: " + data[3] + "; \n")
    file.close()
    print("Заметка создана!" + "\n")