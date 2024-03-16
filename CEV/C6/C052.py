# Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
#.

N = int(input('Digite um número: '))

C = 0

print('Os números que dividem {} são: '.format(N))

for c in range(1, N + 1):

    if N % c == 0:
        print('\033[1;34m', end='')
        C += 1

    else:
        print('\033[1;31m', end='')
    print('{} '.format(c), end='')

print('\n\033[mO número {} foi divisível {} vezes'.format(N, C))

if C == 2:
    print('Este número é PRIMO')
else:
    print('Este número NÃO é PRIMO')
