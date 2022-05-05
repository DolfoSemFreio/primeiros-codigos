import time
print('-'*31)
print(f'{"BANCO LOPES":^30}')
print('-'*31)
valor = int(input('Que valor voce quer sacar? R$'))
total = valor
totced = 0
ced = 100
while True:
        if total >= ced:
            total -= ced
            totced += 1
        else:
            if totced > 0:
                print(f'Total de {totced} de R${ced}')
            if ced == 100:
                ced = 50
            elif ced == 50:
                ced = 20
            elif ced == 20:
                ced = 10
            elif ced == 10:
                ced = 5
            elif ced == 5:
                ced = 1
            totced = 0
            if total == 0:
                break
print('-'* 31)
print('Obrigado, volte sempre!')
time.sleep(10)
