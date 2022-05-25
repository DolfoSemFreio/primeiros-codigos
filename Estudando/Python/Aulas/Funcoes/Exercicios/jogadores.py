def ficha(jogador='<desconhecido>', gols=0):
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato.')


print('-'*30)
jogo = input('Nome do jogador: ')
g = input('Numero de gols: ')
if g.isnumeric():
    g = int(g)
else:
    g = 0
if jogo.strip() == '':
    ficha(gols = g)
else:
    ficha(jogo, g)