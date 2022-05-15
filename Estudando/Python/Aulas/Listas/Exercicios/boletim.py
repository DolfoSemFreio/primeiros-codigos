alunos = list()
notas = list()
while True:
    notas.append(input('Nome: '))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    alunos.append(notas[:])
    notas.clear()
    cont = input('Quer continuar? [S/N] ').strip().upper()[0]
    while cont not in 'SN':
        cont = input('Tente novamente. Quer continuar? [S/N] ').strip().upper()[0]
    if cont == 'N':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-'*26)
for i, l in enumerate(alunos):
    media = (l[1] + l[2]) / 2
    print(f'{i:<4}{l[0]:<10}{media:>8.1f}')
print('-'*30)
while True:
    pont = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if pont == 999:
        break
    print(f'Notas de {alunos[pont][0]} sao {alunos[pont][1:3]}')
    print('-'*30)
print('FINALIZANO...')
