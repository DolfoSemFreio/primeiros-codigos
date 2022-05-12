teste = list()
teste.append('Adolfo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
# OU
galera = [['Joao', 18],['Adolfo', 19],['Heloisa', 15]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')
# OU
totmai = totmen = 0
galera = list()
dado = list()
for cont in range(0, 3):
    dado.append(input('Nome: '))
    dado.append(int(input('Idade: ')))
    galera.append(dado [:]) # sempre colocar o [:] porque se nao ele se liga a primeira lista
    dado.clear()
for c in galera:
    if c[1] >= 18:
        print(f'{c[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1    
print(f'Temos {totmai} maiores e {totmen} menores de idade')