from datetime import datetime
atual = datetime.now().year


def voto(nasc):
    idade = atual - nasc
    print(f'Com {idade} anos: ', end='')
    if idade < 16:
        print('Voto negado por não ter a idade mínima.')
    elif 16 <= idade < 18:
        print('O seu voto é opcional.')
    else:
        print('O seu voto é obrigatório por ser maior de idade.')


nasc = int(input('Digite o ano de nascimento: '))
voto(nasc)