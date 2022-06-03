def leiaDinheiro(r):
    valido = False
    while not valido:
        entrada = str(input(r)).strip().replace(',', '.')
        if entrada.isalpha() or entrada == '':
            print(f'ERRO: \"{entrada}\" é um preço invalido!')
        else:
            valido = True
            return float(entrada)