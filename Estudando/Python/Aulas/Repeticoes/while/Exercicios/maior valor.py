cont = soma = media = 0
continua = 'S'
while continua in 'Ss':
    num = int(input('Digite um numero: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    continua = input('Quer continuar? [S/N]: ').upper().strip()
media = soma/cont
print(f'Fim{maior}{menor}{media}')