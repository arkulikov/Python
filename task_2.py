"""
Создать текстовый файл (не программно),
сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.
Примечание: создается файл по результатам работы task_1. Используем его.
"""
try:
    with open("for_task_1.txt", "r", encoding="utf-8") as my_file:
        str_count_all = 0  # общее кол-во строк в файле
        words_count = 0  # общее кол-во слов

        for my_str in my_file:
            my_list = my_str.rstrip().split(" ")  # убираем лишние пробелы и сплитуем строку
            str_count_all += 1
            words_count_in_str = len(my_list)
            words_count += words_count_in_str
            print(f"В строке {str_count_all} число слов {words_count_in_str}")

        print(f"Всего в файле - {str_count_all} строк и {words_count} слов")
except IOError:
    print("Файл не существует!")
