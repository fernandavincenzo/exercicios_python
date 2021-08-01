lista = []
for c in range(0,5):
    novo = (int(input('Digite um valor: ')))
    if c == 0 or novo > lista[-1]:
        lista.append(novo)
        print('Valor adicionado no final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if novo <= lista[pos]:
                lista.insert(pos, novo)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1
print(lista)