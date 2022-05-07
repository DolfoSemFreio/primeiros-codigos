numbs = (int(input('Digite um numero: ')),
         int(input('Digite outro numero: ')),
         int(input('Digite mais um numero: ')),
         int(input('Digite o ultimo numero: '))
         )
print(f'Voce digitou os valores {numbs}')
print(f'O valor 9 apareceu {numbs.count(9)} vezes')
if 3 in numbs:
    print(f'O valor 3 apareceu na posicao {numbs.index(3) + 1}')
else:
    print('O valor 3 nao apareceu')
print(f'Os valores pares digitados foram ', end='')
for n in numbs:
    if n % 2 == 0:
        print(n, end=' ')
