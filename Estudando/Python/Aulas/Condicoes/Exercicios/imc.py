alt = float(input('Qual é a sua altura: '))
weigth = float(input('Qual é o seu peso: '))
imc = weigth / (alt ** 2)
print(f'O seu IMC é de {imc:.1f}')
if imc <= 18.5:
    print(f'Abaixo do peso')
elif imc >= 18.5 and imc <= 25:
    print('Peso ideal')
elif imc >= 25 and imc <= 30:
    print('Sobrepeso')
elif imc >= 30 and imc <= 40:
    print('Obesidade')
elif imc >= 40:
    print('Obesidade Morbida')
