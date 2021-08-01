from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range (1,8):
    nasc = int(input('{} - Digite seu ano de nascimento:'.format(c)))
    idade = atual - nasc
    if idade>18:
        maior += 1
    else:
        menor +=1
print('Temos {} pessoas maiores de idade.'.format((maior)))
print('Temos {} pessoas menores de idade.'.format(menor))