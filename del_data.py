def delete_note():
    print("Заметку можно удалить по номеру ID")
    with open("data.txt") as file:
        id_del = int(input())
        id_note = file.readlines()
        # if id_del <= len(id_note):
        #     del id_note[id_del - 1]
        #     # with open("data.txt", "w") as file:
        #     #     for item in id_note:
        #     #         file.read(item)
        # else:
        #     print("такого номера строки нет")
        print(id_note)

