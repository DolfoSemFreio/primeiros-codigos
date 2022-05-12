lista = []
par = []
impar = []
while True:
    var = int(input('Digite um valor: '))
    lista.append(var)
    if var % 2 == 0:
        par.append(var)
    elif var % 2 == 1:
        impar.append(var)
    
    cont = input('Quer continuar? [S/N] ').strip().upper()[0]
    while cont not in 'NS':
        cont = input('Tente novamente. Quer continuar? [S/N] ').strip().upper()[0]  
    if cont == 'N':
        break
par.sort()
impar.sort()
print('-'*30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de impares é {impar}')

