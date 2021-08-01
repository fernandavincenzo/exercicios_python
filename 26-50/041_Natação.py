from datetime import date
print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO: CATEGORIAS')
anoatual = date.today().year
anonasc = int(input('Digite aqui seu ano de nascimento: '))
idade = anoatual - anonasc
print('Você tem {} anos.'.format(idade))
if idade<=9:
    print('A categoria com base na sua idade é a Mirim.')
elif idade<=14:
    print('A categoria com base na sua idade é a Infantil.')
#não é necessário colocar que é a idade é maior que 9, o porgrama já identifica se ele não se encaixa no if1
elif idade<=19:
    print('A categoria com base na sua idade é a Junior.')
elif idade<=25:
    print('A categoria com base na sua idade é a Sênior.')
else:
    print('A categoria com base na sua idade é a Master')
