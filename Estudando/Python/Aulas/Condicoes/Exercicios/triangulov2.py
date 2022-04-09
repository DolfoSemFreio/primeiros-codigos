print('\033[31m-='*20)
print('        \033[36mAnalisador de triagulos')
print('\033[31m-=\033[0m'*20)
n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os segmentos acima PODEM formar um triagulo', end=' ') #aparentemente end='' serve para o texto do printi continar na mesma linha
    if n1 == n2 == n3:
        print('EQUILATERO')
    elif n1 == n2 or n2 == n3 or n3 == n1:
        print('ISOSCELES')
    elif n1 != n2 and n3 != n2 and n3 != n1:
        print('ESCALENO')
else:
    print('Os segmentos acima NAO PODEM formar um triangulo')
