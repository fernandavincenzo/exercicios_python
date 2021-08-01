import math
co = float(input('Insira o comprimento do cateto oposto: '))
ca = float(input('Insira o comprimento do cateto adjacescente: '))
print('O comprimento da hipotenusa desse triângulo retângulo {:.2f}'.format(math.hypot(co, ca)))
