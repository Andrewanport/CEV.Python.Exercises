"""""
Exercício Python 088: 
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, 
cadastrando tudo em uma lista composta.
"""""

# imports
from random import randint
from time import sleep

# Design
print('<>'*25)
print('                \033[33mJOGO DO TIGRINHO\033[m                ')
print('<>'*25)

l = list()
j = list()

quant = int(input('Digite quantos jogos devem ser sorteados: '))

tot = 1

while tot <= quant:
    count = 0
    while True:
        num = randint(1, 99)

        if num not in l:
            l.append(num)
            count += 1

        if count >= 6:
            break
    l.sort()
    j.append(l[:])
    l.clear()
    tot += 1

for i, e in enumerate(j):
    print(f'Jogo {i+1}: {e}')
    sleep(1)

# Design
print('<>'*25)
print('              \033[33mA CASA SEMPRE VENCE! \033[m               ')
print('<>'*25)
