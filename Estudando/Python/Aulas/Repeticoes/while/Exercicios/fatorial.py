from math import factorial
n = int(input('Digite um numero: '))
f = factorial(n)
while n > 0:
    print(f'{n}', end='')
    print(' x ' if n > 1 else ' = ', end='')
    n -= 1
print(f'{f}')