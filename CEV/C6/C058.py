"""

Exercício Python 058:
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.

"""

from random import randint
from time import sleep

print('Pensando...')

sleep(3)

print('-'*60)
print('Consegue adivinhar o número que estou pensando de 1 - 10? ')
print('-'*60)

A = randint(1, 10)

P = int(input('Digite o seu palpite: '))

C = 1

while P != A:

    P = int(input('Errado! Tente novamente: '))
    C += 1

print('Correto! Você precisou de {} tentativa(s)!'.format(C))
