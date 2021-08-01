total = c = 0
num = int(input('Digite um número [999 para parar o programa]: '))
while num != 999:
    total += num
    c += 1
    num = int(input('Digite um número [999 para parar o programa]: '))
print('Você digitou {} números válidos e a soma entre eles é de {}'.format(c, total))
