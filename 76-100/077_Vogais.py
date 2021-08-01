palavras = ('fernanda', 'luiz', 'joao', 'carla',
            'belle', 'casa', 'flor', 'caderno',
            'cachorro', 'gato', 'coelho')
for item in palavras:
    print(f'\nNa palavra {item.upper()} temos ', end='')
    for letra in item:
        if letra.lower() in 'aeiou':
            print(f'- {letra}', end=' ')