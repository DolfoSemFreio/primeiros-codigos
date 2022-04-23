stop = cont = soma = 0 # caso todos recebam 0
stop = int(input('Digite um numero [999 para parar]: ')) # coloquei aqui fora pq caso a resposta seja 999 ele n faca o while
while stop != 999:
        soma += stop
        cont += 1
        stop = int(input('Digite um numero [999 para parar]: '))
print(f'Voce digitou {cont} numeors e a soma entre eles foi {soma}')