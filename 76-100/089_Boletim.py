stop = ''
dados = []
while True:
    nome = input('Nome: ')
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    dados.append([nome, [n1, n2], media])
    stop = input('Deseja parar o cadastro? [S/N]').upper()[0]
    if stop == 'S':
        break

print(f'\n{"N°:":<4}{"Aluno:":<15}{"Média:"}')
for a in range(0, len(dados)):
    print(f'{a:<4}{dados[a][0]:<15}{dados[a][2]:.2f}')
while True:
    aluno = int(input('\nMostrar notas de qual aluno? [999 para interromper]'))
    if aluno == 999:
        print('Muito obrigada por utilizar o programa!')
        break
    if aluno <= len(dados)-1:
        print(f'Notas de {dados[aluno][0]} são {dados[aluno][1]}')