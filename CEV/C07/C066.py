"""
Exercício Python 066:
Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas
(desconsiderando o flag).
"""

N = 0
Q = 0
S = 0
C = 1

while True:

    N = int(input(f'Digite um número ({C}): '))
    C += 1

    if N == 999:
        break

    else:
        S += N
        Q += 1

print(f'Você digitou {Q} número(s) e a soma entre eles foi de {S}')
