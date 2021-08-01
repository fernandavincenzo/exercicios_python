num = int(input('Digite um número inteiro: '))
print('''Escolha uma base para conversão:
Digite 1: converter para BINÁRIO
Digite 2: converter para OCTAL
Digite 3: converter para HEXADECIMAL''')
opcao = int(input('Digite sua escolha: '))
if opcao == 1:
    print('{} convertido para binário = {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para octal = {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para hexadecimal = {}'.format(num, hex(num)[2:]))
else:
    print('Opção escolhida inválida.')
