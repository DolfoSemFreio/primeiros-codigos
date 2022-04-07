n1 = float(input('Primeiro Trimeste: '))
n2 = float(input('Segundo Trimestre: '))
n3 = float(input('Terceiro Trimestre: '))
media = (n1 + n2 + n3) / 3
if media > 6:
    print(f'Voce foi \033[1:32mAPROVADO\033[0m com uma media de {media:.1f}')
elif media > 4.5 < 6.0:
    print(f'Voce esta de \033[1:33mRECUPERACAO\033[0m com uma media de {media:.1f}')
elif media < 4.5:
    print(f'Voce esta \033[1:31mREPROVADO\033[0m sua media anual foi de {media:.1f}')
else:
    print('Valores invalidos')