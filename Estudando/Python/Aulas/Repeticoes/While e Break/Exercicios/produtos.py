print('-'*40)
print('          LOJA SUPER BARATAO')
print('-'*40)
res = barato = ''
preco = tot = menor = totmil = cont = 0
while True:
    produto = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preco: R$ '))
    res = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    cont += 1
    tot += preco
    if preco > 1000:
        totmil += 1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    while res not in 'SN':
        res = input('Ivalido tente novamente, mas so use [S/N] ').strip().upper()[0]
    if res == 'N':
        break
print('-'*6, 'FIM DO PROGAMA', '-'*6)
print(f'O total da compra foi R${tot:.2f}')
print(f'{totmil} produtos custam acima de R$1000')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}. ')
