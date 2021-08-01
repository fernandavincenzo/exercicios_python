n1 = int(input('Insira aqui o primeiro número: '))
n2 = int(input('Agora, insira aqui o segundo número: '))
if n1>n2:
    print('O primeiro número, de valor {}, é maior que o segundo número, de valor {}.'.format(n1, n2))
elif n2>n1:
    print('O segundo número, de valor {}, é maior que o primeiro número, de valor {}.'.format(n2, n1))
else:
    print('O primeiro e o segundo número são iguais, pois ambos têm o valor {}.'.format(n1))
