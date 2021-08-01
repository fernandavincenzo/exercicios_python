n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
menu = 0
while menu != 5:
    print('''Digite:
[ 1 ] para somar os números
[ 2 ] para multiplicar os números
[ 3 ] para conferir o maior
[ 4 ] adicionar outros números diferentes
[ 5 ] sair do programa ''')
    menu = int(input('Escolha: '))
    if menu == 1:
        print('{} + {} = {}'.format(n1, n2, n1+n2))
    elif menu == 2:
        print('{} x {} = {}'.format(n1, n2, n1 * n2))
    elif menu == 3:
        if n1 > n2:
            print('{} é maior que {}'.format(n1, n2))
        else:
            print('{} é maior que {}'.format(n2, n1))
    elif menu == 4:
        print('Insira novos números')
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
    elif menu == 5:
        print('Finalizando o programa...')
    else:
        print('OPÇÃO INVÁLIDA. Insira uma opção novamente.')
print('FIM! Muito obrigado por usar o programa!')
