# Вычислить число c заданной точностью *d*

q = int(input('Введите заданную точность числа пи: '))
pi = 3.1415926535
template = '{:.' + str(q) + 'f}'
print(template.format(pi))

