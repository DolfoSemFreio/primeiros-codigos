dicionario = dict()
situacao = ''
dicionario['nome'] = input('Nome: ')
dicionario['media'] = float(input(f'Media de {dicionario["nome"]}: '))
if dicionario['media'] > 7.0:
    dicionario['situacao'] = 'Aprovado'
elif 5 <= dicionario['media'] < 7:
    dicionario['situacao'] = 'Recuperacao'
else: 
    dicionario['situacao'] = 'Reprovado'
print('-='*30)
for v, k in dicionario.items():
    print(f'  - {v} é igual a {k}')