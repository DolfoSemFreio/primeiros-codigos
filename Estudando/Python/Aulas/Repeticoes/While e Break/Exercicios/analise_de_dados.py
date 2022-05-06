idade = cont = homem = mulher = 0
sexo = ''

while True:
    print('-'*25)
    print('   CADASTRE UMA PESSOA')
    print('-'*25)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = input('Sexo: [M/F]').strip().upper()[0]
    prox = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while prox not in 'SN':
                prox = input('Sim ou Nao? ').strip().upper()[0]
    if idade >= 18:
        cont += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade >= 20:
        mulher += 1
    if prox == 'N':
        break
print(f'O total de pessoas com mais de 18 anos: {cont}')
print(f'Ao todo temos {homem} homens cadastrados.')
print(f'Ao todo {mulher} mulheres com menos de 20 anos')