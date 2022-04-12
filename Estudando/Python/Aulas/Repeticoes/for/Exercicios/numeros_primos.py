n1 = int(input('Digite um numero: '))
tot = 0
for c in range(1, n1+1):
    if n1 % c == 0:
        print(f'\033[33m{c}', end=' ')
        tot += 1
    else:
        print(f'\033[31m{c}', end=' ')
print(f'\n\033[mO numero {n1} foi divisivel {tot} vezes.', end='')