print('CARRINHO DE COMPRAS: ')
c = menor = total = mil = 0
nomemenor = ''
while True:
    c += 1
    nome = str(input('Digite o nome do produto: ')).strip()
    preco = float(input('Digite o preço do produto: R$'))
    total += preco
    if preco > 1000:
        mil += 1
    if c == 1 or preco < menor:
        menor = preco
        nomemenor = nome
    play = ' '
    while play != 'N' and play != 'S':
        play = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if play == 'N':
        break
print(f'O total da compra foi: R${total:.2f}')
print(f'Há {mil} produtos que custam mais de R$1000,00 no seu carrinho.')
print(f'O produto mais barato foi {nomemenor} que custa R${menor:.2f}')
