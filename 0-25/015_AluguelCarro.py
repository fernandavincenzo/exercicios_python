dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos Km foram rodados nesse tempo? '))
total = (dias*60)+(0.15*km)
print('O total a ser pago de aluguel é de R${:.2f}'.format(total))
