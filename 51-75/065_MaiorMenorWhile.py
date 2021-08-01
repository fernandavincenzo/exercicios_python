mais = 'S'
c = total = 0
while mais == 'S':
    num = int(input('Digite um número: '))
    c += 1
    total += num
    if c == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    mais = str(input('Quer continuar? [S/N]')).strip().upper()[0]
media = total/c
print('O valor média dos {} números é de {}. O valor {} é o maior, enquanto {} é o menor.'.format(c, media, maior, menor))
