lista = []
impares = []
pares = []
while True:
    lista.append(int(input('Digite um valor para adicionar na lista: ')))
    stop = input('Deseja parar o cadastro de números? [S/N] ').upper()[0]
    if stop == 'S':
        break

for c, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

print(f'A lista dos números é: {lista}')
print(f'A lista dos números pares é: {pares}')
print(f'A lista dos números ímpares é: {impares}')