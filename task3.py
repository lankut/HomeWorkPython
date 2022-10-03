# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.
# Минимальное значение дробной части отличное от нуля, у целых чисел дробной части нет их в расчет не берем.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import math

list_num = [1.1, 1.2, 3.1, 5, 10.01, 188.66, 19]
list_new = []

for i in range(0, len(list_num)):
    list_new.append(list_num[i]-int(list_num[i]))


min = list_new[0]
max = list_new[0]

for i in range(0, len(list_new)):
        if list_new[i] !=0 and list_new[i] < min:
            min = list_new[i]
        if list_new[i] > max:
            max = list_new[i]
        diffr = max - min

print(list_num)
print(list_new)
print(round((min), 2))
print(round((max), 2))
print(f'Разница между максимальным и минимальным значением {round((max), 2)} и {round((min), 2)} составляет: {round((diffr), 2)}')
