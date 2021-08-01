cid = str(input('Digite o nome de sua cidade: ')).strip()
santo = (cid[:5].upper() == 'SANTO')
print('Há a palavra "Santo" no começo do nome de sua cidade? {}'.format(santo))
