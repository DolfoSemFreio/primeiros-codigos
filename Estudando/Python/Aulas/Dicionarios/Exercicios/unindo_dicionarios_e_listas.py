soma = media = 0
dici = dict()
lista = list()
while True:
    dici['nome'] = input('Nome: ').strip()
    dici['sexo'] = input('Sexo: ').strip().upper()[0]
    while dici['sexo'] not in 'MF':
        dici['sexo'] = input('ERRO! Por favor, digite apenas M ou F').strip().upper()[0]
    dici['idade'] = int(input('Idade: ').strip())
    soma += dici['idade']
    con = input('Quer continuar? [S/N] ').strip().upper()[0]
    while con not in 'SN':
        con = input('ERRO! Por favor, digite apenas S ou N').strip().upper()[0]
    lista.append(dici.copy())
    if con == 'N':
        break
media = soma / len(lista)
print('-='*40)
print(f'A)  Ao todo temos {len(lista)} pessoas cadastradas.')
print(f'B)  A media de idade é de {media}.')
print('C)  As mulheres cadastradas foram ', end='')
for p in lista:
    if p['sexo'] in 'F':
        print(f'{p["nome"]} ', end='')
print()  
print('D) Uma lista de pessoas com idade acima da média ')  
for p in lista:
    if p['idade'] >= media:
        print('      ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')