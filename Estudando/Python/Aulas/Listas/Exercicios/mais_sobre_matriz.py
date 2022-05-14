matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
spar = mai = somacol = 0
for i in range(0, 3):
    for l in range(0, 3):
        matriz[i][l] = int(input(f'Digite um valor par [{i}, {l}]: '))
print('-'*30)
for i in range(0, 3):
    for l in range(0, 3):
        print(f'[{matriz[i][l]:^5}]', end='')
        if matriz[i][l] % 2 == 0:
            spar += matriz[i][l]
    print()
print('-'*30)
print(f'A soma dos valores pares é {spar}')
for l in range(0, 3):
    somacol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {somacol}')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}')