# lista = [2, 5, 8, 9]
# lista[2] = 3
# lista.append(7)
# lista.sort(reverse=True)
# lista.insert(2, 2)
# if 4 in lista:
#     lista.remove(4)
# else:
#     print('Nao achei o numero 4')
# print(lista)
# print(f'Essa lista tem {len(lista)} elementos')
valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posicao {c} encontrei o valor {v}.')
print('Cheguei ao final do progama')
