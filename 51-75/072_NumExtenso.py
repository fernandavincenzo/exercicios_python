numeros = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', \
          'treze', 'catorze', 'quinze', 'dezesseis', 'dezesste', 'dezoito', 'dezenove', 'vinte'
play = 'S'
while play == 'S':
    while True:
        num = int(input('Digite um número de 0 à 20: '))
        if 0 <= num <=20:
            break
    print(f'Você digitou {numeros[num]}')
    play = str(input('Você deseja continuar? [S/N]')).strip().upper()[0]
print('Muito obrigado por utilizar o programa!')
