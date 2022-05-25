def ficha(jogador='<desconhecido>', gol = 0):
    dic['nome'] = jogador
    dic['gols'] = gol
    lista.append(dic.copy())

    
lista = []
dic = {}
while True:    
    joga = input('Nome do jogador: ').strip()
    g = input('Numero de gols: ')
    if g.isnumeric():
        g = int(g)
    else:
        g = 0
    if joga == '':
        ficha(gol=g)
    else:
        ficha(joga, g)
    cont = input('Quer continuar? [S/N] ').strip().upper()[0]
    while cont not in 'SN':
        cont = input('Tente novamente. Quer continuar? [S/N] ').strip().upper()[0]
    if cont == 'N':
        break
print('-='*15)
print('cod ', end='')
for c in dic.keys():
    print(f'{c:<14} ',end='')
print()
print('-='*15)
for n, g in enumerate(lista):
    print(f'{n:>3} ', end='')
    for i in g.values():
        print(f'{i:<15}', end='')
    print()
    print('-='*15)
    