km = float(input('\033[32mQual a velocidade do seu carro? \033[m'))
if km>80.0:
    multa = (km-80)*7
    print('-=-'*35)
    print('\033[31mOps, parece que você está dirigindo acima do limite de velocidade! Você deve pagar R${:.2f} de multa.\033[m'.format(multa))
    print('-=-'*35)
print('\033[32mBoa viagem e dirija sempre em segurança!\033[m')
