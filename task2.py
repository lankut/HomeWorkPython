# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16]
# - [2, 3, 5, 6] => [12, 15]

list_num = [2, 3, 4, 5, 6, 8, 9]

list_print = []
l_half = int(len(list_num)/2+1)

k = 1
for i in range (0, l_half):
    if i <= len(list_num)-k:
        list_print.append(list_num[i]*(list_num[len(list_num)-k]))
        k+=1

print(list_num)
print(f'Список из произведения пар сходящихся к центру: {list_print}')
