from random import randint
acertou = False
palpites = 0
pc = randint(0, 50)
print('''Sou seu computador...
Acabei de pensar em um numero entre 0 e 50.
Sera que voce consegue advinhar qual foi?''')

while not acertou:
    you = int(input('Qual é o seu palpite? '))
    if you <= 50:
        palpites += 1
        if you == pc:
            acertou = True
        else:
            if you < pc:
                print('Mais... Tente mais uma vez.')
            elif you > pc:
                print('Menos... Tente mais uma vez')
    else:
        print('Apenas numeros entre 0 a 50.')
print(f'Acertou  com {palpites} tentativas. Parabens!')

