gol = []
dici = {}
dici['nome'] = input('Nome do jogador: ')
a = int(input(f'Quantas partidas {dici["nome"]} jogou?'))
for c in range(0, a):
    gol.append(int(input(f'Quantos gols na partida {c}? ')))
dici['gols'] = gol[:]
dici['total'] = sum(gol)
print('-='*40)
print(dici)
print('-='*40)
for c, n in dici.items():
    print(f'O campo {c} tem o valor {n}.')
print('-='*40)
print(f'O jogador {dici["nome"]} jogou {a} partidas.')
for i, t in enumerate(dici['gols']):
    print(f'  => Na partida {i}, fez {t} gols.')
print(f'foi um total de {dici["total"]}')