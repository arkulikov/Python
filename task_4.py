"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""


rus_numb = ('Один ', 'Два ', 'Три ', 'Четыре ')

my_f = open('for_lesson_4.txt', "r", encoding='utf-8')
my_f_two = open('to_lesson_4.txt', 'a', encoding='utf-8')

for line in my_f:
    my_str_for_wr = ''
    my_tup = line.partition('-')
    if my_tup[0] == 'One ':
        my_str_for_wr = rus_numb[0] + my_tup[1] + my_tup[2]
    elif my_tup[0] == 'Two ':
        my_str_for_wr = rus_numb[1] + my_tup[1] + my_tup[2]
    elif my_tup[0] == 'Three ':
        my_str_for_wr = rus_numb[2] + my_tup[1] + my_tup[2]
    elif my_tup[0] == 'Four ':
        my_str_for_wr = rus_numb[3] + my_tup[1] + my_tup[2]
    my_f_two.write(my_str_for_wr)

my_f.close()
my_f_two.close()
