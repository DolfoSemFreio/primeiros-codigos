somidade = 0
media = 0
nomevelho = ''
maioridadehomem = 0
totmulher = 0
for c in range(1, 5):
    print(f'----- {c} PESSOA -----')
    name = input('Nome: ').strip()
    idade = int(input('Idade: '))
    Sexo = input('Sexo [M/F]: ').strip()
    somidade += idade
    if c == 1 and Sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = name
    if Sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = name
    if Sexo in 'Ff' and idade < 20:
        totmulher += 1
media = somidade / 4
print(f'A media de idade do grupo é de {media} anos.')
print(f'O homem mais velho tem {maioridadehomem} e se chama {nomevelho}.')
print(f'Ao todo sao {totmulher} mulheres com menos de 20 anos.')
