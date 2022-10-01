# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

def mult(x):
    if x == 1:
        return 1
    else:
        return x * mult(x - 1)

num = int(input('Введите число: '))

list = []
for i in range (1, num + 1):
    list.append(mult(i))

print(list)