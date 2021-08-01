num = int(input('Por favor, digite um número de 0 à 9999:  '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('O algarismo das unidades é {}'.format(u))
print('O algarismo das dezenas é {}'.format(d))
print('O algarismo das centenas é {}'.format(c))
print('O algarismo dos milhares é {}'.format(m))
