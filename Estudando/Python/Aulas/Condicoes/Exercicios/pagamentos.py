print('='*10,'\033[34mLOPES ATACADO\033[0m','='*10)
price = float(input('Preco das compras: R$'))
istallments = int(input('''FORMAS DE PAGAMENTO
[ 1 ] á vista dinheiro/pix
[ 2 ] á vista no cartao
[ 3 ] 2x no cartao
[ 4 ] 3 ou mais vezes no cartao
Qual é a sua opcao? '''))
if istallments == 1:
    novo = price - (price * 10 / 100)
    print(f'Sua compra de R${price:.2f} saira por R${novo:.2f} no final')
elif istallments == 2:
    novo = price - (price * 5 / 100)
    print(f'Sua compra de R${price:.2f} saira por R${novo:.2f} no final')
elif istallments == 3:
    novo = price / 2
    print(f'Sua compra de R${price:.2f} saira em 2 vezes de R${novo:.2f} no final')
elif istallments == 4:
    vezes = int(input('Em quantas vezes? '))
    novo = price + (price * 20 / 100)
    if vezes <= 24:
        parcela = novo / vezes
        print(f'A sua compra parcelada saira por {novo:.2f} com cada parcela no valor de {parcela:.2f}')
    else:
        print('So parcelamos em até 24x')