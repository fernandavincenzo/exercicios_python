n1 = float(input('Digite aqui a sua primeira nota: '))
n2 = float(input('Digite aqui a sua segunda nota: '))
m = (n1+n2)/2
print('A sua média final foi {:.2f}'.format(m))
if m>=7:
    print('Parabéns! Você foi aprovado!')
elif m<5:
    print('Infelizmente você está reprovado.')
else:
    print('Você não foi reprovado, mas está de recuperação.')