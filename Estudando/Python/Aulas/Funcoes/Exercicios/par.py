def par(num):
    if num % 2 == 0:
        return True
    else:
        return False


n1 = int(input('Digite um valor: '))
if par(n1):
    print('É par')
else:
    print('Nao é par')