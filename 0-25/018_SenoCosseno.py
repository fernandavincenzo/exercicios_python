import math
ang = float(input('Digite o ângulo desejado: '))
seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))
print('O ângulo de {:.2f} tem o seno de {:.2f}'.format(ang, seno))
print('O ângulo de {:.2f} tem o cosseno de {:.2f}'.format(ang, cosseno))
print('O ângulo de {:.2f} tem a tangente de {:.2f}'.format(ang, tangente))
