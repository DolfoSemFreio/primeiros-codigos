primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
decimo = primeiro + (10-1) * razao #formula para saber os 10 primeiros numeros, se quiser saber os 20 primeiros basta trocar o 10 por 20
for c in range(primeiro, decimo, razao):
    print(f'{c}', end=' » ')
print('Acabou!')