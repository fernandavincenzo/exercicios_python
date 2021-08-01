s = 0
scont = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        s = s + c
        scont = scont + 1
print('A soma de todos os números ímpares múltiplos de 3 é {}'.format(s))
print('Temos {} números nessa adição'.format(scont))
