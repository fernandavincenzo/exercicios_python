from datetime import datetime
dados = dict()

dados['nome'] = input('Nome: ')
nasc = (int(input('Ano de Nascimento: ')))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 se não tem): '))
if dados['ctps'] == 0:
    print('Muito obrigada por utilizar o programa!')
else:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$'))
    dados['aposentadoria'] = (dados['contratação']+35) - nasc

print()

for k, v in dados.items():
    print(f'{k}: {v}')