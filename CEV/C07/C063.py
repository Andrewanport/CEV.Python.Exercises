"""
Exercício Python 063:
Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma
Sequência de Fibonacci.

Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8
"""

print(22 * '-')
print('SEQUÊNCIA DE FIBONACCI')
print(22 * '-')

N = int(input('Digite quantos termos deseja mostrar: '))

A1 = 0
A2 = 1
A3 = A1 + A2

print('{} -> {}'.format(A1,A2), end='')

C = 3

while C <= N:
    print(' -> {}'.format(A3),end='')
    C += 1

    A1 = A2
    A2 = A3
    A3 = A1 + A2

print('-> END')
