"""
Создать текстовый файл (не программно).
Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
Выполнить подсчёт средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""
from statistics import mean

try:
    with open("for_lesson_3", "r", encoding="utf-8") as my_file:
        small_salary, salaries = [], []

        for my_str in my_file:
            my_list = my_str.rstrip().split(" ")
            salaries.append(float(my_list[1]))
            if float(my_list[1]) < 20000:
                small_salary.append(my_list[0])

        print(f"Эти сотрудники имеют низкую зарплату - {small_salary}")
        print(f"Средний доход сотрудников: {mean(salaries)}")
except IOError:
    print("Файл не существует!")
