"""
Exercício Python 064:
Crie um programa que leia vários números inteiros p,elo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
"""
# Inicializadores

N = 0
C = 0
S = 0

while N != 999:

    N = int(input('Digite um número qualquer [999 para parar]: '))

    # Número de números recebidos
    C += 1

    # Soma dos números recebidos
    S += N

print('A quatidade de número digitados foi de : {}'.format(C-1))
print('A soma de número digitados foi de : {}'.format(S-999))
