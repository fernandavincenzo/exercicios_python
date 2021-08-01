n = int(input('Digite quantos termos quer mostrar: '))
t1 = 0
t2 = 1
c = 3
print('{} -> {}'.format(t1, t2), end=' -> ')
while c <= n:
    c += 1
    t3 = t1 + t2
    print(t3, end=' -> ')
    t1 = t2
    t2 = t3
print('FIM')