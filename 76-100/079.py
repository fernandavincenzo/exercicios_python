valores = list()
while True:
    novo = (int(input('Digite um valor para adicionar na lista: ')))
    if novo in valores:
        print('Valor já cadastrado, pulando... ')
    else:
        valores.append(novo)
    stop = input('Deseja parar o cadastro de números? [S/N] ').upper()[0]
    if stop == 'S':
        break
valores.sort()
print(f'Os valores únicos cadastrados foram: {valores}')