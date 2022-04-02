from random import randint
computador = randint(0, 10)
print('-=-' * 15)
print('Em que numero entre 0 a 10 eu estou pensando?')
print('-=-' * 15)
player = int(input(''))
if computador == player:
    print(f'Quentissimo filho, tu acertou!')
else:
    print(f'Erouuuuuuuu, tava pensando no {computador}')