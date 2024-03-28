
from random import randint
from time import sleep

print('-'*60)
print('Consegue adivinhar o número que estou pensando de 1 - 10? ')
print('-'*60)

A = randint(1,10)

P = int(input('Digite o seu palpite: '))

print('-'*60)

print('Carregando...')
sleep(1.5)

print('-'*60)

if A == P:
    print('Você acertou! O número que pensei foi {}'.format(A))

else:
    print('Você errou! O número que pensei foi {}'.format(A))