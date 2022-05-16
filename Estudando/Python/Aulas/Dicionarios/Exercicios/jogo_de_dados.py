from random import randint
from time import sleep
from operator import itemgetter
dic = { 
}
lista = list()
for i in range(1, 6):
    dic[f'jogador{i}'] = randint(1, 6)
for k, v in dic.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
print('-='*40)
print('  == RANKING DOS JOGADORES ==')
ranking = sorted(dic.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'    {i+1} lugar: {v[0]} com {v[1]}')
    sleep(1)