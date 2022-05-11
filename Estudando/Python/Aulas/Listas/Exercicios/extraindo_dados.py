lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    cont = input('Quer continuar? [S/N]? ').strip().lower()[0]
    while cont not in 'sn':
        cont = input('Tente novamente. Quer continuar? [S/N] ').strip().lower()[0]
    if cont == 'n':
        break
print('-*30')
print(f'Voce digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores decrescentes sao {lista}')
if 5 in lista:
    print(f'O valor 5 foi encontrado na lista')
else:
    print(f'O valor 5 nao foi encontrado na lista')