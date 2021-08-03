from random import randint
from operator import itemgetter
jogadores = dict()
ranking = list()
print('Valores Sorteados:')
for c in range(1, 5):
    jogadores[f'jogador{c}'] = randint(1, 6)

for k, v in jogadores.items():
    print(f'O {k} tirou {v}')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('\nRanking dos jogadores:')
for k, v in enumerate(ranking):
    print(f'{k+1}° lugar: {v[0]}, com {v[1]} pontos')
