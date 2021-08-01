r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
if r2<r1+r3 and r1<r2+r3 and r3<r1+r2:
    print('Essa retas conseguem formar um triângulo!')
else:
    print('Essas retas não podem formar um triângulo...')