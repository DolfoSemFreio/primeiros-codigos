casa = float(input('Qual o valor do imovel: R$'))
salario = float(input('Qual é o seu salario: R$'))
ano = int(input('Pretende financiar em quantos anos? '))
sal = salario * 0.30
imov = casa / (ano * 12)
if imov <= sal:
    print('Emprestivo \033[32mAPROVADO')
else:
    print('Emprestimo \033[31mNEGADO')

