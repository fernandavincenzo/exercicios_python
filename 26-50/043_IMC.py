print('CONSULTA DE IMC')
alt = float(input('Digite aqui sua altura em metros: '))
peso = float(input('Agora digite aqui seu peso em kilogramas: '))
imc = peso/(alt**2)
print('O seu Índice de Massa Corporal é de {:.2f}'.format(imc))
if imc<18.5:
    print('Tenha cuidado! Você está abaixo do peso ideal para sua altura.')
elif imc<25:
    print('Você está com o peso ideal para sua altura.')
elif imc<30:
    print('Tenha cuidado! Você está com sobrepeso.')
elif imc<40:
    print('Tenha cuidado! Você está com obesidade.')
else:
    print('Tenha cuidado! Você está com obesidade mórbida.')