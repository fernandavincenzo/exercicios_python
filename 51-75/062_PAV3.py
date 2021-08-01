num = int(input('Digite o primerio termo: '))
razao = int(input('Digite a razão: '))
c = 1
mais = 10
termos = 0
while mais != 0:
    termos += mais
    while c <= termos:
        print(num, end=' - ')
        num += razao
        c += 1
    print('PAUSA')
    mais = int(input('\nDeseja mais quantos termos? '))
print('Muito obrigada por utilizar o programa! Ao total foram {} termos.'.format(termos))
