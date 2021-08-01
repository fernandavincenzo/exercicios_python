total = 0
maior = 0
menos20 = 0
nomeh = ''
for c in range(1, 5):
    print('{}° PESSOA:'.format(c))
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO (f/m): ')).strip().lower()
    total += idade
    if c == 1 and sexo == 'm':
        maior = idade
        nomeh = nome
    elif idade > maior and sexo == 'm':
        maior = idade
        nomeh = nome
    if sexo == 'f' and idade < 20:
        menos20 += 1
print('A média de idade do grupo é de {} anos'.format(total/4))
print('O homem mais velho do grupo se chama {} e tem {} anos'.format(nomeh, maior))
print('Neste grupo há {} mulheres com menos de 20 anos.'.format(menos20))
