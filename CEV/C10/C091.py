"""""
Exercício Python 091: 
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
Guarde esses resultados em um dicionário em Python. 
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""""

from random import randint
from time import sleep
from operator import itemgetter

Jogadas = {'Jogador 1': randint(1, 6),
           'Jogador 2': randint(1, 6),
           'Jogador 3': randint(1, 6),
           'Jogador 4': randint(1, 6)}

rank = list()

print('Valores sorteados:')

for K, V in Jogadas.items():
    print(f'{K} -> {V}')
    sleep(0.5)

print('_'*30)

rank = sorted(Jogadas.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(rank):
    print(f'{i+1}º lugar -> {v[0]} com {v[1]}')

print('_'*30)

