lista = [[], []]
valor = 0
for c in range(0, 7):
    valor = int(input('Digite um valor:'))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print('-'*30)
lista[0].sort()
lista[1].sort()
print(f'Os valores pares sao {lista[0]}')
print(f'Os valores impares sao {lista[1]}')