from time import sleep
import defs

preco = float(input('Digite o preço: '))

while True:
    try:
        taxa = float(input('Taxa: '))
        break
    except ValueError:
        print('Por favor, insira uma taxa.')
print(f'A metade de {defs.moeda(preco)} é {defs.moeda(defs.metade(preco))}')
sleep(1)
print(f'O dobro de {defs.moeda(preco)} é {defs.moeda(defs.dobro(preco))}')
sleep(1)
print(f'Aumentando {taxa:.0f}%, temos {defs.moeda(defs.aumentando(preco, taxa))}')