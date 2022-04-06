num = int(input('Digite um numero inteiro: '))
print("""Escolha uma das bases para conversao:
[ 1 ] BINARIO
[ 2 ] OCTAL
[ 3 ] HEXADECIMAL""")
opcao = int(input('Sua opcao: '))
if opcao == 1:
    print(f'{num} Convertido para BINARIO é {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} Convertido para OCTAL é {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} Convetido para HEXADECIMAL {hex(num)[2:]}')
else:
    print('Opcao invalida tente novamente')