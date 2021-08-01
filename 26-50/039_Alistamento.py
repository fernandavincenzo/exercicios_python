from datetime import date
genero = int(input('Sobre seu genero: digite 0 para masculino ou 1 para feminino: '))
if genero == 0:
    ano = int(input('Insira aqui o seu ano de nascimento: '))
    anoatual = date.today().year
    idade = anoatual-ano
    print('Em {} você estará completando {} anos.'.format(anoatual, idade))
    if idade<18:
        anos=18-idade
        print('Você ainda não precisa se alistar. Falta {} anos para que seja necessário.'.format(anos))
    elif idade==18:
        print('Este ano é necessário que você se apresente para o alistamento!')
    elif idade>18:
        anos=idade-18
        print('Já passou o ano de seu alistamento. Faz {} anos que passou o prazo.'.format(anos))
else:
    print('Por seu gênero, não é necessário que você se aliste no exército')
        