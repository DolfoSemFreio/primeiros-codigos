media = 0
qnt = 1
loop = True
maior = 0
menor = 0
soma = 0
while loop == True:
    print('-=-' * 9)
    n = int(input(f'digite o número {qnt}: '))
    c = str(input('quer continuar? [Y/N] ')).upper()
    print('-=-' * 9)

    if c == 'y'.upper():
        print('ok, continue.')
        qnt += 1
    elif c == 'n'.upper():
        loop = False
    else:
        print('\033[1;31mReinicie e digite um valor valido.\033[m')
        break
    media += n

    if n < menor or menor == 0:
        menor = n
    if n > maior or maior == 0:
        maior = n
print(f'A média dos valores é {media / qnt :.1f}')
print(f'O menor número é {menor}.')
print(f'O maior número e {maior}')