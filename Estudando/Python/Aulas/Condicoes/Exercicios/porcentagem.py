salario = float(input('Qual é o seu salario: '))
if salario > 1250.00:
    novo = salario + (salario * 10 / 100)
else:
    novo = salario + (salario * 15 / 100)
print(f'Quem ganhava R${salario:.2f} passa a ganhar R${novo:.2f}')
print(f'{3 * 5 + 4 ** 2}')
s = 'prova de python'
print(f'{len(s)}')
