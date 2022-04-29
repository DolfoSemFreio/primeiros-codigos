from random import randint

print('=-' * 15)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-' * 15)
v = 0
while True:
    pc = randint(1, 10)
    player = int(input('Diga um valor: '))
    tot = player + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Voce jogou {player} e o computador {pc}. Total de {tot}', 'DEU PAR' if tot % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if tot % 2 == 0:
            print('Voce \033[32mVENCEU!\033[0m')
            v += 1
        else:
            break
    elif tipo == 'I':
        if tot % 2 == 1:
            print('Voce \033[32mVENCEU!\033[0m')
            v += 1
        else:
            break
print(f'''\033[31mGAME OVER!\033[0m
Voce venceu {v} vezes.''')
