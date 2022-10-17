# Создайте программу для игры в 'Крестики-нолики'.

position=[]
for i in range(1,10):
    position.append(i)

sign = '0'

while True:
    if sign == '0':
        sign = 'x'
    else:
        sign = '0'
    print(f'{position[0]:^5}|{position[1]:^5}|{position[2]:^5}')
    print('-----------------')
    print(f'{position[3]:^5}|{position[4]:^5}|{position[5]:^5}')
    print('-----------------')
    print(f'{position[6]:^5}|{position[7]:^5}|{position[8]:^5}')

    index = int(input(f"\n\nХод {'игрока' if sign == 'x' else 'противника'}: "))

    position[index-1] = sign
