z = int(input('Valor inicial: '))
y = int(input('Valor final: '))
soma = 0
cont = 0
for c in range(z, y, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print(f'A soma de todos os {cont} valores divisiveis por 3 é {soma}')