def metade(a=0):
    s = a / 2
    return s


def dobro(a=0):
    s = a * 2
    return s


def aumentando(a=0, taxa=10):
    s = (a * taxa/100) + a
    return s

def moeda(a=0, moeda = 'R$'):
    return f'{moeda}{a:>.2f}'.replace('.', ',')