"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyError(Exception):
    def __init__(self, txt):
        self.text = txt


def division():
    one = input('Введите первое число: ')
    two = input('Введите второе число: ')

    try:
        a = int(one)
        b = int(two)
        if b == 0:
            raise MyError('Делить на ноль нельзя!!!')
        res = a / b
    except ValueError:
        print('Вы ввели не число!')
    except MyError as err:
        print(err)
    else:
        print(f"Результат деления: {res}")


division()
