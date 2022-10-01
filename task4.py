# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов
# на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint

def get_numbers(x):
    list = []
    for i in range(-x, x):
        list.append(randint(-x, x))
    return list

path = 'file.txt'
data = open(path, 'r')
list2 = [int(line.strip()) for line in data]
data.close()

number = get_numbers(10)

print(number)
print(list2)

def res(number, list2):
    mult = 1
    for i in list2:
        mult *= number[i]
    return mult

print(res(number, list2))
