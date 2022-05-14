from random import randint
from time import sleep
print('-'*30)
print('      JOGO NA MEGA SENNA')
print('-'*30)
lista = list()
lista2 = list()
jogos = int(input('Quantos jogos voce quer que eu sorteie? '))
tot = 1
print(f'-=-=-= SORTEANDO {jogos} JOGOS =-=-=-')
while tot <= jogos:
    cont = 0
    while True:
        numbs = randint(1, 60)
        if numbs not in lista:
            lista.append(numbs)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    lista2.append(lista[:])
    lista.clear()
    tot += 1
for i, l in enumerate(lista2):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
    
