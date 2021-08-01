num = (int(input('Digite um valor de 0 à 10: ')),
    int(input('Digite um valor de 0 à 10: ')),
    int(input('Digite um valor de 0 à 10: ')),
    int(input('Digite um valor de 0 à 10: ')))
print(f'Os números escolhidos foram: {num}')
print(f'O número 9 foi digitado {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 foi digitado pela primeira vez na posição: {num.index(3)+1}')
else:
    print('o número 3 não foi digitado.')
print('Os números pares digitados foram: ', end='')
for n in num:
    if n % 2 ==0:
        print(n, end=' ')