tupla = ('Lapis', 1.75,
         'Borracha', 2,
         'Caderno', 15.90,
         'Estojo', 25,
         'Transferidor', 4.20,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.30,
         'Livros', 34.90)
print('-'*40)
print(f'{"LISTAGEM DE PRECOS":^40}')
print('-'*40)
for item in range(0, len(tupla)):
    if item % 2 == 0:
        print(f'{tupla[item]:.<30}', end='')
    else:
        print(f'R${tupla[item]:>7.2f}')
print('-'*40 )