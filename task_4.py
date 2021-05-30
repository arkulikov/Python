"""
Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""


def my_func_one(x, y):
    res = x ** y
    print(res)
    return


def my_func_two(x, y):
    x, y = float(x), int(y)
    res = x
    for _ in range(abs(y) - 1):
        res *= x
    return 1 / res


my_func_one(4, -2)
print(my_func_two(4, -2))

