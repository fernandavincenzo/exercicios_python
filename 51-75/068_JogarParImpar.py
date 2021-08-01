from random import randint
c = 0
while True:
    pi = str(input('Escolha: Par ou Impar? [P/I] ')).strip().upper()[0]
    while pi not in 'PI':
        pi = str(input('Escolha: Par ou Impar? [P/I] ')).strip().upper()[0]
    jogador = int(input('Ok, escolha sua jogada (de 0 à 5): '))
    pc = randint(0, 5)
    soma = pc+jogador
    print(f'Eu joguei {pc} e você jogou {jogador}. Total: {soma}.')
    if pi == 'P':
        if soma % 2 == 0:
            print('PAR! Você venceu!')
            print('Vamos jogar novamente!')
            c += 1
        else:
            print('ÍMPAR! Você perdeu!')
            print(f'Você teve {c} vitórias consecutivas!')
            break
    if pi == 'I':
        if soma % 2 != 0:
            print('ÍMPAR! Você venceu!')
            print('Vamos jogar novamente!')
            c += 1
        else:
            print('PAR! Você perdeu!')
            print(f'Você teve {c} vitórias consecutivas!')
            break
