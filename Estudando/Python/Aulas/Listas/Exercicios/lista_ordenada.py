import time
lista = []
for i in range(0, 5):
    var = int(input('Digite um valor: '))
    if i == 0 or var > lista[-1]:   
        lista.append(var)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if var <= lista[pos]:
                lista.insert(pos, var)
                print(f'Adicionado na posicao {pos} da lista...')
                break
        pos += 1
print('-'*30)
print(f'Os valores foram adicionados na posicao {lista}.')
time.sleep(10)