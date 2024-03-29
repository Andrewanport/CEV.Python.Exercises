"""
Exercício Python 068:
Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""

# Imports
from random import randint
from time import sleep

# Intro
print(21*'-')
print('JOGO DO PAR OU ÍMPAR!')
print(21*'-')

# Win counter
W = 0

while True:

    # User Input
    U = int(input('Digite um número inteiro: '))
    E = str(input('Escolha Par ou Ímpar [P/I]: ')).strip().upper()[0]

    while E not in 'PI':
        E = str(input('Escolha Par ou Ímpar [P/I]: ')).strip().upper()[0]

    print(40 * '-')

    # Random Input
    C = randint(0, 10)

    # Output 1
    print('O computador está escolhendo um número...')

    # Delay
    sleep(2)

    # Sum
    S = U + C

    # Result
    R = ''

    if S % 2 == 0:
        R = 'PAR'
    else:
        R = 'ÍMPAR'

    print(60 * '-')

    print(f'Você jogou {U} e o computador jogou {C}. A soma deu {S} que é {R}')

    if S % 2 == 0 and E == 'I' or S % 2 != 0 and E == 'P':
        break

    if S % 2 == 0 and E == 'P' or S % 2 != 0 and E == 'I':
        print(60 * '-')
        print('Você venceu! Vamos jogar novamente...')
        print(35 * '-')

        W += 1

# Output
print(21 * '-')
print(f'Você venceu {W} vez(es)')
print(21 * '-')
print('\033[1;31mGAME OVER')
