matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = c3 = 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        if c == 2:
            c3 += matriz[l][c]

for l in range(0,3):
    for c in range(0,3):
        print(f'[ {matriz[l][c]} ]', end='')
    print()

max = max(matriz[1])

print(f'A soma dos valores da terceira coluna é {c3}.')
print(f'A soma dos valores pares é {pares}.')
print(f'O maior valor da segunda linha é {max}.')