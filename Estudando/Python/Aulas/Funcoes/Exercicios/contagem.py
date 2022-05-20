from time import sleep
def contar(num1, num2, passo):
    print(f'Contando de {num1} até {num2} de {passo}')
    
    if num1 < num2:
        cont = num1
        while cont <= num2:
            print(f'{cont} ', end='', flush=True) # flush serve para o sleep aparecer na tela sem delay
            sleep(0.5)
            cont += passo
        print('Fim!')
    else:
        cont = num1
        while cont >= num2:
            print(f'{cont} ', end='', flush=True) 
            sleep(0.5)
            cont -= passo
        print('Fim!')

print('-='*30)
contar(1, 10, 1)
print('-='*30)
contar(10, 0, 2)
print('-='*30)
print('Agora é a sua vez de personalizar a contagem!')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contar(i, f, p)
