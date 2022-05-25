def fatorial(num=1, show=False):
    """
    -> Calcula o fatorial de um numero

    Args:
        num (int, optional): Numero a ser calculado. Defaults to 1.
        show (bool, optional): Se vai ou nao mostrar a conta. Defaults to False.

    Returns:
        retorna o resultado do fatorial
    """
    f=1
    for c in range(num, 0, -1):   
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c    
    return f

print(fatorial(6, True))