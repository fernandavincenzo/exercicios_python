def maior(*num):
    if len(num) == 0:
        print(f'Não há nenhum número passado')
    else:
        print(f'O maior número de {num} é {max(num)}')


maior(3,6,9,5,2,4,99)
maior(4, 7, 0)
maior()