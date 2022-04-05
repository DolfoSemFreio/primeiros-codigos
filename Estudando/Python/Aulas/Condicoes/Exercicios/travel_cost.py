k = float(input('Qual é a distancia da sua viagem: '))
print(f'Voce esta prestes a comecar uma viagem de {k:.2f}Km.')
if k > 200:
    print(f'E o preco da sua passagem sera de R${k * 0.45:.2f}')
else:
    print(f'E o preco da sua passagem sera de R${k * 0.50:.2f}')
