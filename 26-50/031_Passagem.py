km = float(input('Qual é a distância da sua viagem em quilômetros? '))
if km>200:
    v = km*0.45
    print('O valor da sua passagem será de R${:.2f}.'.format(v))
else:
    v = km*0.5
    print('O valor da sua passagem será de R${:.2f}.'.format(v))