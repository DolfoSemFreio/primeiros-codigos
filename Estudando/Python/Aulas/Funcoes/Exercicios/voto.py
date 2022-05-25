def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NAO VOTA.'
    elif 16 >= idade < 18 or idade > 60:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    
    
# Programa principal
nasc = int(input('Em que ano voce nasceu: '))
print(voto(nasc))