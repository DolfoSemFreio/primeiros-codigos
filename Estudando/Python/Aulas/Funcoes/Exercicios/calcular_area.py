def calcular(largu, compri):
    s = largu * compri
    print(f'A area de um terreno de {largu}x{compri} é de {s}m²')

#Programa principal
print('-'*20)
print('CONTROLE DE TERRENOS')
num1 = float(input('Largura(m) '))
num2 = float(input('Comprimento(m) '))
calcular(num1, num2)