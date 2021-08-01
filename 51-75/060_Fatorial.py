# maneira de se fazer com modulos (muito mais facil mds pra q while???):
from math import factorial
num = int(input('Digite um número: '))
fatorial = factorial(num)
print('O fatorial de {} é {}'.format(num, fatorial))

# maneira de se fazer com while (apenas para praticar puff):
num = int(input('Digite um número para achar seu fatorial: '))
f = 1
print('{}! = '.format(num), end='')
while num > 0:
    print(num, end='')
    print(' x ' if num > 1 else ' = ', end='')
    f *= num
    num -= 1
print(f)
