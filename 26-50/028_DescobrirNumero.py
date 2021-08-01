from random import randint
from random import randint
from time import sleep
nome = str(input('\033[33mQual é o seu nome? '))
print('Seja muito bem vinde, {}! Vamos jogar um jogo?\033[m'.format(nome))
print('{}-=-{}'.format('\033[34m','\033[m')*25)
print('\033[31mEscolha um número de 0 à 5, se você acertar em qual estou pensando, ganha!\033[m')
print('{}-=-{}'.format('\033[34m','\033[m')*25)
pc = randint(0,5)
num = int(input('\033[33mEm qual número estou pensando? '))
print('PROCESSANDO...\033[m')
sleep(2)
if num == pc:
    print('\033[32mParabéns, você acertou o número que estava pensando. WIN!\033[m')
else:
    print('\033[31mAh, que pena... Você não acertou o número, era {}. GAME OVER!\033[m'.format(pc))
