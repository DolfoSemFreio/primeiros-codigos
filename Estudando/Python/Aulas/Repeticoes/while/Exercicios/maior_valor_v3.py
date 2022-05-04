cont = soma = media = 0
res = 'S'
while res in 'S':
    num = int(input('Digite um numero: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if  num < menor:
            menor = num
    res = input('Quer continuar? [S/N] ').strip().upper()
media = soma / cont
print(f'Voce digitou {cont} numeros e a media foi {media}')
print(f'O maior valor foi o {maior} e o menor foi {menor}')