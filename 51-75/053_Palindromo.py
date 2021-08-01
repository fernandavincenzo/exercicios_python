frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
juncao = ''.join(palavras)
inverso = juncao[::-1]
#for c in range(len(juncao)-1, -1, -1):
 #   inverso += juncao[c]
if inverso == juncao:
    print('{} e {} são iguais, portanto, palíndromos.'.format(juncao, inverso))
else:
    print('{} e {} não são iguais, portanto, não são palíndromos.'.format(juncao, inverso))