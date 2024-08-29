"""""
Exercício Python 073: 
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela da Champions, na ordem de colocação. Depois mostre:
    
a) Os 4 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o Manchester City.
"""""

Times = ('Real Madrid', 'Borussia', 'Bayern', 'PSG', 'Manchester City', 'Barcelona', 'Arsenal', 'Atlético de Madrid')

print(150*'~')

print(f'Os 8 melhores times da champions são: {Times}')

print(150*'~')

print(f'Os 4 primeiros colocados da Champions, são: {Times[0:5]}')

print(110*'~')

print(f'Os 4 últimos colocados da Champions, são: {Times[-4:]}')

print(110*'~')

print(f'A ordem alfabética dos times é: {sorted(Times)}')

print(150*'~')

print(f'O Manchester City está na {(Times.index("Manchester City")) + 1}ª posição')
