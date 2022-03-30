name = input('Digite uma frase: ').strip

print(f'A letra A aparece: {name.count("a")}')
print(f'A primeira letra A apareceu na posicao: {name.find("a")+2}')
print(f'A ultima letra A apareceu na posicao: {name.rfind("a")+2}')