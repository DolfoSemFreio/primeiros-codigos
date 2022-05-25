def ficha(jogador='<desconhecido>', gol = 0):
    print(f'O jogador {jogador} fez {gol} gol(s) no campeonato.')
    
    
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
      