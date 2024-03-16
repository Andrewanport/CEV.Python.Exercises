# Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
# .

N = int(input('Digite um número inteiro: '))

if N % 2 == 0:
    print('O número {} é par!'.format(N))

else:
    print('O número {} é ímpar!'.format(N))