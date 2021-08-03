jogador = dict()
gols = list()
jogador['nome'] = input('Nome do Jogador: ')
partidas = int(input('Partidas jogadas: '))
for c in range(0, partidas):
    gols.append(int(input(f'Gols na partida {c+1}: ')))

jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print()
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas: ')
for c, g in enumerate(jogador['gols']):
    print(f'Na partida {c+1}, fez {g} gols.')
print(f'Foi um total de {jogador["total"]} gols.')