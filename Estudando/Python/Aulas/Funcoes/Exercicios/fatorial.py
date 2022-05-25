def fatorial(num=1, show=False):
    """
    => Calcula o fatorial de um numero

    Args:
        num (int, optional): Numero a ser fatorado. Defaults to 1.
        show (bool, optional): Mostra ou nao a conta. Defaults to False.

    Returns:
        _type_: Retorna o valor do calculo
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

# Programa principal
fato = int(input('Numero a ser fatorado: '))
cont = input('Quer ver a conta: [S/N] ').upper().strip()[0]
if cont == 'S':
    cont = True
elif cont == 'N':
    cont = False
print(fatorial(fato, cont))
            