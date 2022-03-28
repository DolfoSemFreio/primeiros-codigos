n1 = float(input('Qual o preço do produto? R$ '))
n2 = float(input('O desconto é de quantos porcentos? '))
des = n2/100*n1
res = n1 - des
print(f'O produto que custava R${n1}, na promocao com desconto de {n2:.0f}% vai custar R${res:.2f}.')
