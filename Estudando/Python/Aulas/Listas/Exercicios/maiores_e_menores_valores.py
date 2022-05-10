lista = []
mai = men = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posicao {c}: ')))
    if c == 0:
        mai = men = lista[c]
    else:
        if lista[c] > mai:
            mai = lista[c]
        if lista[c] < men:
            men = lista[c]
print('-='*50)
print(f'Voce digitou os numeros {lista}')
print(f'O maior valor digitado foi o {mai} nas posicoes ', end = '')
for i, v in enumerate(lista):
    if v == mai:
        print(f'{i}...', end = '')
print()
print(f'O menor valor digitado foi o {men} nas posicoes ', end = '')
for i, v in enumerate(lista):
    if v == men:
        print(f'{i}...', end='')
print()