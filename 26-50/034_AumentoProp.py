s = float(input('Digite o seu salário: R$'))
if s>1250:
    a = s*10/100
    nv = s+a
    print('O valor de seu aumento é de R${:.2f}, e o seu novo salário é de R${:.2f}.'.format(a,nv))
else:
    a = s*15/100
    nv = s+a
    print('O valor de seu aumento é de R${:.2f}, e o seu novo salário é de R${:.2f}.'.format(a,nv))
    