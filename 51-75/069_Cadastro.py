c = maiores = homens = mulheres20 = 0
while True:
    c += 1
    print(f'Cadastro da {c}° pessoa:')
    idade = int(input('Digite sua idade: '))
    sexo = ' '
    while sexo != 'F' and sexo != 'M':
        sexo = str(input('Digite seu sexo [F/M]: ')).strip().upper()[0]
    if idade >= 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade<20:
        mulheres20 += 1
    play = ' '
    while play != 'N' and play != 'S':
        play = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if play == 'N':
        break
print(f'No grupo há {maiores} pessoas maiores de idade.')
print(f'Foram cadastrados {homens} homens, e {mulheres20} mulheres com menos de 20 anos.')
print('Muito obrigada por utilizar o programa! ')