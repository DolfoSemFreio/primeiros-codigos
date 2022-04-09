from random import randint
from time import sleep #da um daley ao soltar os textos para o terminal
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Sua opcoes:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
player = int(input('Qual é a sua escolha: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-='*11)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[player]}')
print('-='*11)
if computador == 0: #computador jogou tesoura
    if player == 0:
        print('EMPATE')
    elif player == 1:
        print('JOGADOR VENCE')
    elif player == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVALIDA')
elif computador == 1: # computador jogou papel
    if player == 0:
        print('COMPUTADOR VENCE')
    elif player == 1:
        print('EMPATE')
    elif player == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVALIDA')
elif computador == 2: #Computador jogou tesoura
    if player == 0:
        print('JOGADOR VENCE')
    elif player == 1:
        print('COMPUTADOR VENCE')
    elif player == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')
