def contador(i, f, p):
    """ -> Faz uma contagem e mostra na tela

    Args:
        i (Inicio): Inicio da contagem
        f (Fim): Final da contagem
        p (Passo): Passo da contagem
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('Fim')
