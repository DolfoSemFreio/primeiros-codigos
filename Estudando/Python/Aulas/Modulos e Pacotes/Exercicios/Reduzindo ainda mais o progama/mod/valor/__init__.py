def resumo(p, add, des):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)
    print(f'Preço analisado:  R${p:.2f}')
    print(dobro(p))
    print(metade(p))
    print(aumentando(p, add))
    print(diminuindo(p, des))
    

def dobro(p):
    s = p * 2
    
    return f'Dobro do preço: R${s:.2f}'
    
def metade(p):
    s = p / 2
    
    return f'Metade do preço: R${s:.2f}'


def aumentando(p, a):
    s =  p * (a / 100) + p
    
    return f'{a}% de aumento: R${s:.2f}'


def diminuindo(p, des):
    s = p - p * (des/ 100)
    
    return f'{des}% de redução: R${s:.2f}'