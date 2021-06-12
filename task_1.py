"""
Создать программный файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных будет свидетельствовать пустая строка.
"""


def write_to_file():
    while True:
        my_str = input("Введите строку: ")
        if my_str == "":
            break
        else:
            with open("for_task_1.txt", "a", encoding="utf-8") as my_file:
                my_file.write(my_str + '\n')


write_to_file()
