vel = int(input('Qual é a velocidade atual do veiculo? '))
if vel > 80:
    print('Velocidade acima do permitido, voce sera multado')
    multa = (vel - 80) * 7
    print(f'Voce deve parar uma multa de R${multa:.2f}!')
elif vel < 40:
    print('Velocidade muito abaixo da via')
else:
    print('Velocidade permitida')
print('Tenha um bom dia! Dirija com seguranca!')