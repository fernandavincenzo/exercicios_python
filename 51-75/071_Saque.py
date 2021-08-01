saque = int(input('Digite o valor do saque: R$'))
tudo = saque
ced = 50
ceds = 0
while True:
    if tudo >= ced:
        tudo -= ced
        ceds += 1
    else:
        if ceds > 0:
            print(f'{ceds} cédulas de R$ {ced}')
        if tudo == 0:
            break
        ceds = 0
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
print('Final')
