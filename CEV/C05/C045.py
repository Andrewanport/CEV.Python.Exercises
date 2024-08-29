# Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.
# .

from random import randint

I = ('Pedra', 'Papel','Tesoura')

A = randint(0,2)

print((10 * '=') + ' PEDRA, PAPEL OU TESOURA ' + (10 * '='))

print('[0] PEDRA'
      '\n[1] PAPEL'
      '\n[2] TESOURA')

print((10 * '=') + ' SELECIONE SUA JOGADA ! ' + (10 * '='))

J = int(input(''))

if 0 <= J <= 2:

    print('Você jogou: {}'.format(I[J]))
    print('Computador jogou: {}'.format(I[A]))

    # ========== EMPATE ========== #

    if J == A:
        print('Empate!')

    # ========== JOGADOR PEDRA ========== #

    elif J == 0 and A == 2:
        print('\033[1;32mVocê VENCEU!')

    elif J == 0 and A == 1:
        print('\033[1;31mVocê PERDEU!')

    # ========== JOGADOR PAPEL ========== #

    elif J == 1 and A == 0:
        print('\033[1;32mVocê VENCEU!')

    elif J == 1 and A == 2:
        print('\033[1;31mVocê PERDEU!')

    # ========== JOGADOR TESOURA ========== #

    elif J == 2 and A == 1:
        print('\033[1;32mVocê VENCEU!')

    elif J == 2 and A == 0:
        print('\033[1;31mVocê PERDEU!')

else:
    print('\033[1;31mJogada inválida, tente novamente.')
