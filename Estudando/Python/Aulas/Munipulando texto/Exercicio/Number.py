numb = input('Digite um numero de 0 a 9999: ')
if(len(numb) > 4 or len(numb) == 0):
    print('Digite um numero de até 4 digitos')
else:
    print(f'Analisando o numero {numb}')
    print(f'Unidade: {numb[3]}')
    print(f'Dezena: {numb[2]}')
    print(f'Centena: {numb[1]}')
    print(f'Milhar: {numb[0]}')



