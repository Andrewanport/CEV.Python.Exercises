# Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
# .

from math import radians, sin, cos, tan

A = float(input('Digite um ângulo: '))

S = sin(radians(A))
C = cos(radians(A))
T = tan(radians(A))

print('O ângulo {:.2f}º tem o seno de: {:.2f}'.format(A, S))
print('O ângulo {:.2f}º tem o cosseno de: {:.2f}'.format(A, C))
print('O ângulo {:.2f}º tem o tangente de: {:.2f}'.format(A, T))

