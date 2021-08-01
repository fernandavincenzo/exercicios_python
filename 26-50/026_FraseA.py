frase = str(input('Por favor, digite uma frase: ')).upper().strip()
print('A quantidade de vezes que "a" aparece nessa frase é {}.'.format(frase.count('A')))
print('A primeira vez que "a" apareceu nessa frase é na posição {}.'.format(frase.find('A')+1))
print('A última vez que "a" apareceu nessa frase é na posição {}.'.format(frase.rfind('A')+1))
