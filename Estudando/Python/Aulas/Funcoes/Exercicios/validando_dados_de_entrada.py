def leiaInt(numb):
    print('-'*30)
    t = input(numb)
    while True:
        if t.isnumeric():
            return t
        else:
            print('\033[31mERRO! Digite um numero inteiro valido.\033[m')
            t = input(numb)
    
# Programa principal
n = leiaInt('Digite um numero: ')
print(f'Voce acabou de digitar o numero {n}.')