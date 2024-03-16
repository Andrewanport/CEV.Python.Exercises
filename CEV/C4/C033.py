# Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
# .

N1 = int(input('Digite um número inteiro (1):'))
N2 = int(input('Digite um número inteiro (2):'))
N3 = int(input('Digite um número inteiro (3):'))

# ---------------------- Condições para o Maior ---------------------- #

if N1 > N2 and N1 > N3:

    Maior = N1

if N2 > N1 and N2 > N3:

    Maior = N2

if N3 > N2 and N3 > N1:

    Maior = N3

print('O maior número é {}'.format(Maior))

# ---------------------- Condições para o Menor ---------------------- #

if N1 < N2 and N1 < N3:

    Menor = N1

if N2 < N1 and N2 < N3:

    Menor = N2

if N3 < N2 and N3 < N1:

    Menor = N3

print('O menor número é {}'.format(Menor))

