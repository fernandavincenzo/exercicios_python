while True:
    num = int(input('Digite o número para ver sua tabuada: '))
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num}x{c}={num * c}')
print('Final do programa.')
