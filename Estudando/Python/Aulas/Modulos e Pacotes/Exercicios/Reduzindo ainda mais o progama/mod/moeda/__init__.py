def aumentando(a=0, taxa=10, formato = False):
    s = (a * taxa/100) + a
    return s if formato is False else moeda(s)


def metade(a=0, formato = False):
    s = a / 2
    return s if not formato is False else moeda(s)


def dobro(a=0, formato = False):
    s = a * 2
    return s if not formato is False else moeda(s)


def moeda(a=0, moeda = 'R$'):
    return f'{moeda}{a:>.2f}'.replace('.', ',')