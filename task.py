# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

def sum_number (x):
    sum = 0
    while (x!=0):
        num_1= x%10
        sum+=num_1
        x=x//10
    return sum

num = int(input('Введите число для вычисления суммы его чисел: '))

print(sum_number(num))
