# Задача №33: Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от -100 до 100) многочлена и записать в файл многочлен степени k.

import random

k = int(input('Введите значение натуральной степени: '))
print(k)

list = []

for i in range(k):
    list.append(random.randint(-100, 100))
print(list)

list_2 = f'k = {k} -> '

for i in range(len(list)):
    if i != len(list) - 1 and list[i] != 0 and i != len(list) - 2:
        list_2 += f'{list[i]}x^{len(list)-i-1}'
        if list[i+1] != 0 and list[i+1] > 0:
            list_2 += '+'
    elif i == len(list) - 2 and list[i] != 0:
        list_2 += f'{list[i]}x'
        if list[i+1] != 0 and list[i+1] > 0:
            list_2 += '+'
    elif i == len(list) - 1 and list[i] != 0:
        list_2 += f'{list[i]} = 0'
    elif i == len(list) - 1 and list[i] == 0:
        list_2 += ' = 0'
print(list_2)

with open ('res.txt', 'w') as file:
    file.write(list_2)
