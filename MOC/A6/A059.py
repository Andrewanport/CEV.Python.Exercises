"""""
Exercício Python 088: 
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, 
cadastrando tudo em uma lista composta.
"""""

# imports
import random
from time import sleep

# Design
print('<>'*25)
print('                \033[33mJOGO DO TIGRINHO\033[m                ')
print('<>'*25)

# input
N = int(input('Digite quantos jogos devem ser sorteados: '))

# counter for print
c = 0

# prints
for i in range(0, N):
    A = random.sample(range(10, 99 + 1), 6)

    print(f'| Jogo [{c+1}]: {A}')
    c += 1
    sleep(1)        # delay

# Design
print('<>'*25)
print('              \033[33mA CASA SEMPRE VENCE! \033[m               ')
print('<>'*25)