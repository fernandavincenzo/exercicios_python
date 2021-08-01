from random import shuffle
n1 = str(input('Qual o nome do primeiro aluno? '))
n2 = str(input('E do segundo? '))
n3 = str(input('E do terceiro? '))
n4 = str(input('E do quarto? '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem escolhida dos alunos para responderem os exercícios é: {}'.format(lista))
