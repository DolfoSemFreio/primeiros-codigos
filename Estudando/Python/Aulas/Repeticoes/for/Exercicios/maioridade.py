from datetime import date
atual = date.today().year
velha = 0
nova = 0
for pess in range(1, 8):
    year = int(input(f'Em que ano a {pess} pessoa nasceu? '))
    idade = atual - year
    if idade >= 21:
        velha += 1
    else:
        nova += 1
print(f'Temos {velha} pessoas maiores de idade')
print(f'Temos {nova} pessoa menores de idade')