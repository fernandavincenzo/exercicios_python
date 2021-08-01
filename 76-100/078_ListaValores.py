numeros = []
for c in range(0,5):
    numeros.append(int(input(f'Digite um valor para a posição {c}: ')))
min = min(numeros)
max = max(numeros)
print(f'A lista formada é: {numeros}')
print(f'O menor número da lista é {min} nas posições ', end='')
for c, v in enumerate(numeros):
    if v == min:
        print(f'{c}...', end='')
print(f'\nO maior número da lista é {max} nas posicões ', end='')
for c, v in enumerate(numeros):
    if v == max:
        print(f'{c}...', end='')