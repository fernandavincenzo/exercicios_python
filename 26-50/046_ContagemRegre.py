from time import sleep
import emojis
print('CONTAGEM REGRESSIVA FOGOS!')
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print(emojis.encode('FOGOS! :fireworks: :tada:'))
