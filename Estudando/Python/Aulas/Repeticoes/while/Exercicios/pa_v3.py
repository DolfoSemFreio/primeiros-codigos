print('\033[36mGerador de PA\033[0m')
print('\033[37m-=\033[0m'*7)
n1 = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
cont = 1
termo = n1
tot = 0
mais = 10
while mais != 0:
    tot = tot + mais
    while cont <= tot:
        print(termo, end=' » ')
        cont += 1
        termo += razao
    print('\033[33mPAUSE\033[0m')
    mais = int(input('Quantos termos quer mostrar a mais? '))
print('\033[31mFIM')