palavras = (
    'Aprender', 'Estudar', 'Progamar',
    'Desenvolver', 'Pilotar', 'Arara Azul',
    'Desenhar', 'Pintar', 'Chorar'
)
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')