name = input('Didite uma frase: ').strip().upper()
palavra = name.split()
junto = ''.join(palavra)
inv = '' # da pra colocar inv = junto[::-1] e tirar o for mas como to aprendendo for deixa ai mesmo
for letra in range(len(junto) - 1, -1, -1):
    inv += junto[letra]
print(f'O inverso de {junto} é {inv}')
if inv == junto:
    print('A frase é um palindromo')
else:
    print('Nao é um palindromo')