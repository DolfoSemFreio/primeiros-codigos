nome = input('Qual é o seu nome: ')
if nome == 'Adolfo':
    print('Que nome bonito')
elif nome == 'Danielle' or nome == 'Vera' or nome == 'Julia':
    print('Seu nome é bem bonito!')
elif nome in 'Ana Julia Heloisa Nicole':
    print('Belo nome feminino')
else:
    print('Nome bem padrao')
print(f'Tenha um bom dia {nome}')