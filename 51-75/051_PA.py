num = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = num + 10 * razao
for c in range(num, decimo, razao):
    print(c, end=' -> ')
print('Final da Progressão Aritmética')
