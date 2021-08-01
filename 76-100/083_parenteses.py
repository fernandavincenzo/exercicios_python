expressao = input('Digite uma expressão: ')
char = []
for simb in expressao:
    if simb == '(':
        char.append('(')
    elif simb == ')':
        if len(char) > 0:
            char.pop()
        else:
            char.append(')')
            break
if len(char) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão não é válida!')