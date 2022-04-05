a = int(input('Primeiro Numero: '))
b = int(input('Segundo Numero: '))
c = int(input('Terceiro Numero: '))
menor = a
maior = a
#O menor
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
#O maior
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print(f'O maior numero digitado foi {maior}')
print(f'O menor valor digitado foi {menor}')