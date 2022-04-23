print('-'*30)
print('\033[36mSequencia de Fibonacci\033[0m')
print('-' * 30)
n1 = int(input('Qauntos termos voce quer mostra? '))
t1 = 0
t2 = 1
print('~'*35)
print(f'{t1} » {t2}', end='')
cont = 3
while cont <= n1:
    t3 = t1 + t2
    print(f' » {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' » Fim')
print('~'*35)
