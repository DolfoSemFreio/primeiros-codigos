def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1        


def mensagem(msg):
    print('-='*30)
    print(msg)
    print('-='*30)


def soma(* num):
    s = 0
    for c in num:
        s += c
    print(f'Somando os valores {num} temos {s}')
# Programa principal
var = input('Quer algo?')
mensagem(var)
valores = [3, 4, 5, 6, 7, 8, 9, 10]
dobra(valores)
print(valores)
soma(1, 3, 4, 5, 6, 7, 8, 9, 10)