from random import randint
from time import sleep


def sorteio(lista):
    print('Sorteando 5 valores ', end ='')
    for c in range(1, 6):
        random = randint(1, 10)
        lista.append(random)
        print(f'{random} ', end='', flush=True)
        sleep(0.5)
    print('Pronto!')
def somarPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Os valores somados dao {soma}')


numbs = []
sorteio(numbs) 
somarPar(numbs)