from random import randint
pc = randint(0, 10)
print('\033[31mEscolha um número de 0 à 10, se você acertar em qual estou pensando, ganha!\033[m')
win = False
vezes = 0
while not win:
    num = int(input('\033[33mEm qual número estou pensando? '))
    vezes += 1
    if num == pc:
        win = True
    else:
        if num < pc:
            print('\033[31mMais... Tente novamente!\033[m')
        else:
            print('\033[31mMenos... Tente novamente!\033[m')
print('\033[32mParabéns, você acertou o número que estava pensando. WIN!')
print('Você precisou de {} tentativas para ganhar o jogo!\033[m'.format(vezes))
