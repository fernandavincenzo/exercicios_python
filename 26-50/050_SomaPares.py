s = 0
cs = 0
for c in range(0, 6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s = s+n
        cs = cs + 1
print('A soma de todos os valores é {}'. format(s))
print('Foram somados {} números'.format(cs))
