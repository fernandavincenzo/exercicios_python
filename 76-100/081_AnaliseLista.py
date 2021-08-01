lista = []
while True:
    lista.append(int(input('Digite um valor para adicionar na lista: ')))
    stop = input('Deseja parar o cadastro de números? [S/N] ').upper()[0]
    if stop == 'S':
        break
lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} números')
print(f'A ordem decrescente dessa lista é: {lista}')
if 5 in lista:
    print('O valor 5 está nesta lista')
else:
    print('O valor 5 não está nesta lista')