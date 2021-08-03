dados = dict()
dados['nome'] = input('Digite o nome do aluno: ')
dados['media'] = float(input(f'Digite a média de {dados["nome"]}: '))
if dados['media'] >= 7:
    dados['situacao'] = 'APROVADO'
else:
    dados['situacao'] = 'REPROVADO'

print(f'\n{"Aluno:":<20}{"Média:":<20}{"Situação:"}')
for v in dados.values():
    print(f'{v:<20}', end='')
