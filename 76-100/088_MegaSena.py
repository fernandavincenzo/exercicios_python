from random import randint
temp = []
jogos = []
quant = int(input('Quantos jogos você quer que eu sorteie? '))
for c in range(1, quant+1):
    while True:
        num = randint(1, 60)
        if num not in temp:
            temp.append(num)
        if len(temp) == 6:
            break
    print(f'Jogo {c}: {temp}')
    jogos.append(temp)
    temp.clear()