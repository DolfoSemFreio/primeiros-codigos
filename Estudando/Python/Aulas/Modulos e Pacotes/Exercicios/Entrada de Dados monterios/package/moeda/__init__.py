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


def diminuindo(p, des):
    s = p - p * (des/ 100)
    
    return f'{des}% de redução: R${s:.2f}'


def resumo(p, add, des):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)
    print(f'Preço analisado:  R${p:.2f}')
    print(dobro(p))
    print(metade(p))
    print(aumentando(p, add))
    print(diminuindo(p, des))
    

