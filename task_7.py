"""
Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка будет содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список.
Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить её в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""

import json


with open("for_lesson_7.txt", "r", encoding="utf-8") as my_f:
    my_all_list = []
    my_dic = {}
    aver_profit_list = []

    for _ in my_f:
        my_list = _.rstrip().split(" ")
        key = my_list[0]  # ключ словаря
        value_profit = int(my_list[2]) - int(my_list[3])
        if value_profit > 0:
            aver_profit_list.append(value_profit)
        my_dic[key] = value_profit

    aver_profit_dic = {'average_profit': sum(aver_profit_list)}

    my_all_list.append(my_dic)
    my_all_list.append(aver_profit_dic)

with open("for_lesson_7.json", "w", encoding="utf-8") as my_f_json:
    json.dump(my_all_list, my_f_json, ensure_ascii=False, sort_keys=False,
              indent=4,
              separators=(',', ': '))
