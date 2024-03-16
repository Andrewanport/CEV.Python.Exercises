# Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
# .

from random import randint

print('-'*60)
print('Consegue adivinhar o número que estou pensando de 1 - 10? ')
print('-'*60)

A = randint(1,10)

P = int(input('Digite o seu palpite: '))

if A == P:
    print('Você acertou! O número que pensei foi {}'.format(A))

else:
    print('Você errou! O número que pensei foi {}'.format(A))