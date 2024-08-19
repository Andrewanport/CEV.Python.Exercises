"""""
Exercício Python 073: 
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela da Champions, na ordem de colocação. Depois mostre:

a) Os 4 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o Manchester City.
"""""

Times = ('Real Madrid', 'Borussia', 'Bayern', 'PSG', 'Manchester City', 'Barcelona', 'Arsenal', 'Atlético de Madrid')

print('Os 4 primeiros colocados da Champions, são: ')
for P in range(0, 4):
    print(Times[P])

print('Os 4 últimos colocados da Champions, são: ')

for U in range(4, 8):
    print(Times[U])

print('A ordem alfabética dos times é: ')

print(sorted(Times))

print(f'O Manchester City está na {(Times.index("Manchester City")) + 1}ª posição')