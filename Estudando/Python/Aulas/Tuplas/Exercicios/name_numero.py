numb = ('zero', 'um', 'dois', 'tres', 'quatro',
        'cinco', 'seis', 'sete',
        'oito', 'nove', 'dez', 'onze',
        'doze', 'treze', 'quatorze',
        'quinze', 'dezessei', 'dezessete',
        'dezoito', 'dezenove', 'vinte')
while True:
    pergunta = int(input('Digite um numero entre 0 e 20: '))
    while pergunta > 20 or pergunta < 0:
        pergunta = int(input('Tente novamente. Digite um numero entre 0 e 20: '))
    print(f'Voce digitou o numero {numb[pergunta]}')
    res = input('Quer continuar? [S/N] ').strip().upper()[0]
    while res not in 'SN':
        res = input('Tente novamente. Quer continuar? [S/N]: ').strip().upper()[0]
    if res == 'N':
        break
print('Progama finalizado, volte sempre!')



