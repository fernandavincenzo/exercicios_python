brasileirao = 'Brangantino', 'Ahtletico-PR', 'Fortaleza', 'Bahia', 'Palmeiras', 'Atlético-GO', 'Atlético-MG',\
    'Flamengo', 'Fluminense', 'Santos', 'Corinthians', 'Ceará SC', 'Internacional', 'Juventude', 'Sport Recife',\
    'Cuiabá', 'São Paulo', 'Chapecoense', 'América-MG', 'Grêmio'
print(f'Tabela do Campeonato Brasileiro de Futebol: \n{brasileirao}')
print('-='*40)
print(f'Os primeiros 5 colocados são: {brasileirao[0:5]}')
print('-='*40)
print(f'Os últimos 4 colocados são: {brasileirao[-4:]}')
print('-='*40)
print(f'Os timesem ordem alfabética: {sorted(brasileirao)}')
print('-='*40)
print(f'O time Chapecoense está na posição {brasileirao.index("Chapecoense")+1}')