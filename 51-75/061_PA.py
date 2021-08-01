num = int(input('Digite o primerio termo: '))
razao = int(input('Digite a razão: '))
c = 1
while c <= 10:
    print(num, end=' - ')
    num += razao
    c += 1
print('\nFim da Progressão Aritmética')