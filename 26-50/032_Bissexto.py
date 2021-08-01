from datetime import date
ano = int(input('Digite o ano desejado para saber se ele é bissexto, se quiser saber o ano atual, digite 0: '))
if ano == 0:
    ano = date.today().year
if ano%4 == 0 and ano%100 != 0 or ano%400 == 0:
    print('O ano {} ano é um ano bissexto!'.format(ano))
else:
    print('O ano {} não é um ano bissexto.'.format(ano))
    