lista = []
while True:
    valor = int(input('Digite um valor: '))
    while valor in lista:
         valor = int(input('Valor ja existente. Digite um valor: '))
    lista.append(valor)
    cont = input('Quer continuar? [S/N] ').strip().upper()
    while cont not in 'NS':
        cont = input('Tente novamente. Quer continuar? [S/N] ').strip().upper()
    if 'N' in cont:
        break
lista.sort()
print(f' {lista}')
    