from random import randint
lista = (randint(0, 10), randint(0, 10), randint(0, 10),
         randint(0, 10), randint(0, 10))
print('Os Valores sorteados foram: ', end= '')
for c in lista:
    print(f'{c}', end=' ')
print(f'\nO maior numero foi o {max(lista)}')
print(f'O menor numero foi o {min(lista)}')
