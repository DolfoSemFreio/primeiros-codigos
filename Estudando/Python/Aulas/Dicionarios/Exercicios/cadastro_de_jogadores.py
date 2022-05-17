time = []
gol = []
dici = {}
while True:
    dici['nome'] = input('Nome do jogador: ')
    a = int(input(f'Quantas partidas {dici["nome"]} jogou?'))
    for c in range(0, a):
        gol.append(int(input(f'Quantos gols na partida {c+1}? ')))
    dici['gols'] = gol[:]
    dici['total'] = sum(gol)
    time.append(dici.copy())
    cont = input('Quer continuar? [S/N] ').strip().upper()
    gol.clear()
    while cont not in 'NS':
        cont = input('Tente novamente. Quer continuar? [S/N] ').strip().upper()
    if cont == 'N':
        break 
print('-='*40)
print('cod ', end='')
for i in dici.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')  
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    busca = int(input('Quer mostrar o dado de qual jogador? (999 para interromper) '))
    if busca == 999:
        break
    while busca >= len(time):
        busca = int(input('ERRO! Jogador nao existe, tente novamente: '))
    if busca != 999:
        print(f'>> LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'     No jogo {i+1} fez {g} gols.')
        print('-'*40)
print('>> VOLTE SEMPRE <<')