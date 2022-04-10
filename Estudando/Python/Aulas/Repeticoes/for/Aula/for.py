nome = int(input('Qual numero dejesa saber a tabuada? '))
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
#for q in range(0, 2):
#    input('DIGIDE UM NOME: ')
for c in range(0, 11):
    print(f'{nome} x {c} = {nome*c}')
print('\033[31mFim!\033[0m')
for x in range(i, f, p):
    print(x)
print('\033[31mFim!\033[0m')
for y in range(10, 0, -1): # o zero é considerado o ultimo numero nesse caso
    print(y)
print('\033[31mFim!\033[0m')
for l in range(0, nome+1):
    print(l)
print('\033[31mFim!\033[0m')
s = 0
for m in range(0 , 4):
    n = int(input('Digite um valor: '))
    s += n #mesma coisa que s = s + n
print(f'O valores somados dao {s}')
