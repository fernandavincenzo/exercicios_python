jogadores = list()
jogador = dict()
gols = list()
stop = ''
while True:
    jogador['nome'] = input('Nome do Jogador: ')
    partidas = int(input('Partidas jogadas: '))
    for c in range(0, partidas):
        gols.append(int(input(f'Gols na partida {c+1}: ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())
    gols.clear()
    stop = input('Deseja parar o programa? [S/N]')[0]
    if stop == 's':
        break

print(f'\n{"N°:":<4}{"Jogador:":<15}{"Gols:":<15}{"Total:":<15}')
for c, j in enumerate(jogadores):
    print(f'{c:<4}', end='')
    for d in j.values():
        print(f'{str(d):<15}', end='')
    print()

while True:
    print()
    busca = int(input('Mostrar dados de qual jogador? [código - 999 para parar] '))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f'ERRO! Não existe jogador com o código {busca}.')
    else:
        print(f'O jogador {jogadores[busca]["nome"]} jogou {len(jogadores[busca]["gols"])} partidas: ')
        for c, g in enumerate(jogadores[busca]['gols']):
                print(f'Na partida {c+1}, fez {g} gols.')
        print(f'Foi um total de {jogadores[busca]["total"]} gols.')
print('Muito obrigada por utilizar o programa!')