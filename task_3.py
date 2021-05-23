"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(a, b, c):
    obj_one = (a, b, c)
    return sum(obj_one) - min(obj_one)


print(my_func(4, 2, 4))
