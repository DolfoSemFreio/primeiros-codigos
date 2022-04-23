print('\033[36m    Gerador de PA\033[0m')
print('- ='*7)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
decimo = primeiro + (11 - 1) * razao
while primeiro != decimo:
    print(primeiro, end=' » ')
    primeiro += razao

print('Acabou!')