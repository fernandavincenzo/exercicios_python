preco = float(input('Digite aqui o preço do produto: R$'))
print('''Qual é a forma de pagamento?
Digite 0: à vista, em dinheiro ou em cheque
Digite 1: à vista no cartão
Digite 2: em até 2x no cartão
Digite 3: em 3x ou mais no cartão''')
pag = int(input('Digite o número da opção escolhida: '))
if pag==0:
    d=preco-(preco*10/100)
    print('Com este tipo de pagamento, você ganha 10% de desconto, ficando assim com o preço do profuto de R${:.2f}'.format(d))
elif pag==1:
    d=preco-(preco*5/100)
    print('Com este tipo de pagamento, você ganha 5% de desconto, ficando assim com o preço do profuto de R${:.2f}'.format(d))
elif pag==2:
    print('Com este tipo de pagamento, o produto continua com seu preço original, de R${:.2f}'.format(preco))
elif pag==3:
    j = preco+(preco*20/100)
    print('Com este tipo de pagamento, o produto sofre um juros de 20%, totalizando R${:.2f}'.format(j))