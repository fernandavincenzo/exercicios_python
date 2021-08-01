from random import choice
n1 = input('Qual o nome do primeiro aluno? ')
n2 = input('E do segundo? ')
n3 = input('E do terceiro? ')
n4 = input('E do quarto? ')
e = choice([n1, n2, n3, n4])
print('O aluno escolhido para apagar a lousa é: {}!'.format(e))
