"""
Создать (программно) текстовый файл,
записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import random


# функция для записи списка в файл
def record_to_file():
    try:
        my_f = open("for_lesson_5.txt", "w", encoding="utf-8")
        numb_list = [random.randrange(0, 50) for _ in range(0, 51, 2)]  # создаем рэндомный список
        str_list = [str(i) + ' ' for i in numb_list]  # переводим элементы списка выше в str
        # и формируем список
        my_f.writelines(str_list)
        my_f.close()
    except IOError:
        print("Ошибка ввода-вывода!")


def sum_numb_from_file():
    try:
        with open("for_lesson_5.txt", "r", encoding="utf-8") as my_f:
            for _ in my_f:
                str_list = _.strip().split(' ')

            numb_list = [int(i) for i in str_list]

            print(f"Сумма всех чисел в файле - {sum(numb_list)}")
    except IOError:
        print("Ошибка ввода-вывода!")


record_to_file()
sum_numb_from_file()
