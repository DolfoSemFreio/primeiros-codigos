pessoas = {
    'nome': 'Adolfo',
    'sexo': 'Masculino',
    'idade': 18
}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos de idade')
print( )
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print( )
pessoas['nome'] = 'Rick'
print()
for k in pessoas.values():
    print(k)
print()
pessoas['idade'] = 22
for p in pessoas.keys():
    print(p)
print()
for c in pessoas.items():
    print(c)
print()
print(f'{"Dicionario dentro de uma lista":>50}')
# Dicionario dentro de uma lista
brasil = list()
estado = dict()
for z in range(0, 3):
    estado['UF'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla do Estado: ').upper()
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()