print('-=-'*12)
print('PROCESSO CADASTRAMENTO EMPRÉSTIMO')
print('-=-'*12)
vcasa = float(input('Qual é o valor da casa? R$'))
salario = float(input('Qual é o salário do comprador? R$'))
anos = int(input('Em quantos anos o comprador deseja pagar o empréstimo? '))
mensal = vcasa/(anos*12)
porcento = mensal*100/salario
if porcento<30:
    print('Analisamos seus dados e concluímos que você pode financiar esta casa!')
elif porcento>=30:
    print('Analisamos os seus dados e concluímos que infelizmente você não poderá financiar esta casa.')
    