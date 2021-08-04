from time import sleep


def contador(i, f, p):
    c = 0
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    if i < f:
        for c in range(i, f+1, p):
            print(c, end=' ')
            sleep(0.5)
            c += 1
        print('Fim')
    if i > f:
        for c in range(i, f-1, -p):
            print(c, end=' ')
            sleep(0.5)
            c += 1
    print('Fim')


i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Intervalo: '))
contador(i, f, p)