# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

list_fib = [0, 1]

num_in = int(input('Введита размер ряда Фибоначчи: '))

for i in range(2, num_in):
    list_fib.append(list_fib[i-1] + list_fib[i-2])

list_rev=[]
l = len(list_fib)
for i in range(1, l):
    if i%2 == 0:
        list_rev.append(list_fib[l-i])
    else:
        list_rev.append(list_fib[l-i]*(-1))

print(list_rev+list_fib)
