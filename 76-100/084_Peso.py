pessoas = []
gente = []
stop = ''
max = min = 0
while True:
    pessoas.append(input('Nome: '))
    pessoas.append((int(input(f'Peso: '))))
    if len(gente) == 0:
        max = min = pessoas[1]
    else:
        if pessoas[1] > max:
            max = pessoas[1]
        if pessoas[1] < min:
            min = pessoas[1]
    gente.append(pessoas[:])
    pessoas.clear()
    stop = input('Deseja parar o cadastro de números? [S/N] ').upper()[0]
    if stop == 'S':
        break

print(f'Foram cadastradas {len(gente)} pessoas')
print(f'O menor peso é {min}kg de ', end='')
for p in gente:
    if p[1] == min:
        print(f'{p[0]}...', end='')
print(f'\nO maior peso é {max}kg de ', end='')
for p in gente:
    if p[1] == max:
        print(f'{p[0]}...', end='')
