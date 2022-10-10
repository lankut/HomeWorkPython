# Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.

list = list(map(int, input("Введите числа через пробел: ").split()))
print(list)
new_list = []
for i in list:
    if i not in new_list:
        new_list.append(i)
print(f'Список из неповторяющихся элементов: {new_list}')