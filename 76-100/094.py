pessoa = dict()
galera = list()
mulheres = list()
velhos = list()
idade = media = 0
stop = ''
while True:
    pessoa.clear()
    pessoa['nome'] = input('Nome: ')
    while True:
        pessoa['sexo'] = input('Sexo [F/M}: ')[0]
        if pessoa['sexo'] in 'fm':
            break
    pessoa['idade'] = int(input('Idade: '))
    idade += pessoa['idade']
    galera.append(pessoa.copy())
    stop = input('Deseja parar o programa? [S/N]').upper()[0]
    if stop == 'S':
        break

for c in range(0, len(galera)):
    if galera[c]['sexo'] == 'f':
        mulheres.append(galera[c]['nome'])

media = idade / len(galera)

for c in range(0, len(galera)):
    if galera[c]['idade'] > media:
        velhos.append(galera[c]['nome'])

print()
print(f'Foram cadastradas {len(galera)} pessoas.')
print(f'A média de idade das pessoas cadastradas foi de {media} anos.')
print(f'As mulheres cadastradas foram: {mulheres}')
print(f'As pessoas que estão acima da média de idade são: {velhos}')

