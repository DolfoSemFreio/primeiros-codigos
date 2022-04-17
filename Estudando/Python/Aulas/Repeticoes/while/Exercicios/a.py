from random import randint
acertou = False
palpite = 0
pc = randint(0, 50)
print('JOGO')
print('Sou seu computador, tente advinhar o numero entre 0 a 50 que eu pensei')
while not acertou:
    you = int(input('Qual o seu palpite? '))
    if you <= 50:
        palpite += 1
        if you == pc:
            acertou = True
        else:
            if you < pc:
                print('Mais... tente novamente.')
            elif you > pc:
                print('Menos... tente novamente.')
    else:
        print('Apenas numeros entre 0 a 50')
print(f'Parabéns, voce acertou depois de {palpite} tentativas.')