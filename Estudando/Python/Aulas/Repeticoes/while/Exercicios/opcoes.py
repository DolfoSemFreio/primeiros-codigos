v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
op = 0
while op != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos numeros
    [ 5 ] sair do progama''')
    op = int(input('>>>Qual é a sua opcao? '))
    if op == 1:
        print(f'{v1} + {v2} = {v1+v1}')
    elif op == 2:
        print(f'{v1} x {v2} = {v1*v2}')
    elif op == 3:
        if v1 < v2:
            maior = v1
        else:
            maior = v1
        print(f'O maior é o {maior}')
    elif op == 4:
        print('Informe os numeros novamente: ')
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo valor: '))
    elif op == 5:
        print('Finalizando...')
    else:
        print('Opcao invalida. Tente novamente.')
    print('-='*14)
print('Fim do progama! Volte sempre!')