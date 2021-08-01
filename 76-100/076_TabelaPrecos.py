produtos = ('Lapis', 2,
            'Borracha', 1.5,
            'Apontador', 4.25,
            'Caneta', 3,
            'Marca-Texto', 6.5)
print('-'*40)
print('Tabela de Preços da Fernanda:')
print('-'*40)
for item in range(0, len(produtos)):
    if item % 2 == 0:
        print(f'{produtos[item]:.<30}', end='')
    else:
        print(f'R${produtos[item]:.2f}')