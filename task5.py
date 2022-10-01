# Реализовать алгоритм перемешивания списка

import random

def numbers(x):
    return [random.randint(0, 50) for i in range(x)]

def shuffle(y):
    return random.shuffle(y)

a = 15

list1 = numbers(a)
print(list1)
shuffle(list1)
print(list1)
