from random import randint
print('BEM VINDO À MAIS UMA PARTIDA DE JOKENPÔ! TENTE ME VENCER!')
print('''Digite:
0 para pedra
1 para papel
2 para tesoura ''')
jogada = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0,2)
jogador = int(input('Escolha sua jogada: '))
print('O computador jogou {}'.format(jogada[pc]))
print('Você escolheu {}'.format(jogada[jogador]))
if pc == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('VOCÊ VENCEU!')
    elif jogador == 2:
        print('VOCÊ PERDEU!')
elif pc == 1:
    if jogador == 0:
        print('VOCÊ PERDEU!')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('VOCÊ VENCEU!')
elif pc == 2:
    if jogador == 0:
        print('VOCÊ GANHOU')
    elif jogador == 1:
        print('VOCÊ PERDEU!')
    elif jogador == 2:
        print('EMPATE')
