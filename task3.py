# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

def mult(x):
    res = (1+1/x)**x
    return res

num = int(input('Введите число: '))

list = []
for i in range (1, num + 1):
    list.append(mult(i))

sum = 0
for e in range (1, num+1):
    sum +=mult(e)

print(list)
print(round(sum,2))
