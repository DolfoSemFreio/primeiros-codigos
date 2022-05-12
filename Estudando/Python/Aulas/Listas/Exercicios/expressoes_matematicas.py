expr = input('Digite a expressão: ')
lista = []
for simb in expr:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão esta valida')
else:
    print('Sua expressão esta errada')
print(lista)