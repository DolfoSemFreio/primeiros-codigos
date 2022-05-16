from datetime import datetime
trab = dict()

trab['nome'] = input('Nome: ')
trab['idade'] = datetime.now().year - int(input('Ano de Nascimeto: ')) 
trab['ctps'] = int(input('Carteira de Trabalho (0 nao tem): '))
if trab['ctps'] != 0:
    trab['contratacao'] = int(input('Ano de Contratacao: ')) 
    trab['salario'] = int(input('Salario: '))
    trab['aposentadoria'] = trab['idade'] + (trab['contratacao'] + 35) - datetime.now().year
print('-='*40)
for f, s in trab.items():
    print(f' - {f} tem o valor {s}')