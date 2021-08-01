sexo = str(input('Digite seu sexo [F/M]: ')).strip().upper()[0]
while sexo != 'F' and sexo != 'M':
    print('Acredito que você tenha digitado errado. Apenas as opções F ou M são aceitas')
    sexo = str(input('Digite novamente seu sexo [F/M]:')).upper().strip()
print('Muito obrigada por participar!')