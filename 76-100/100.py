from random import randint
numeros = list()


def sorteio(list):
    for c in range(0, 5):
        list.append(randint(0, 100))
    print(f'Os números sorteados foram: {list}')


def somarPar(list):
    s = 0
    for v in list:
        if v % 2 == 0:
            s += v
    print(f'A soma dos números pares da lista {numeros} é: {s}')


sorteio(numeros)
somarPar(numeros)