from datetime import date
ano1 = int(input('Ano de nascimeto: '))
atual = date.today().year
idade = atual - ano1
if idade == 18:
    print('Voce se alista esse ano, procure a junta militar mais proxima.')
elif ano1 > atual:
    print('Informe uma data valida!')
elif idade == 19:
    print(f'Voce ja deveria ter se alistado há 1 ano.')
elif idade > 18:
    print(f'Voce ja deveria ter se alistado há {idade - 18} anos.')
elif idade < 18:
    print(f'Ainda faltam {18 - idade} anos para o alistamento')
    print(f'Voce podera se alistar no ano de {ano1+18}')
elif idade == 17:
    print('Ainda falta 1 ano para o alistamento')
    print('Voce podera se alistar no proximo ano')
