from random import randint
tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os números sorteados foram: ', end='')
for num in tupla:
    print(f'{num} ', end='')
print(f'\nO maior valor sorteado foi: {max(tupla)}')
print(f'O menor valor sorteado foi : {min(tupla)}')