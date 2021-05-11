str_user = list(input("Введите строку: "))

i = 0
for el in range(int(len(str_user) / 2)):
    str_user[i], str_user[i + 1] = str_user[i + 1], str_user[i]
    i += 2

print(str_user)
