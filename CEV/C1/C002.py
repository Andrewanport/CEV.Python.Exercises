# Exercício Python 002: Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.
#.

N1 = int(input('Digite um número:'))
N2 = int(input('Digite outro número:'))

S = N1 + N2

# A forma menos otimizada seria:
# print('A soma entre', N1, 'e', N2, 'vale', S)

# A forma mais inteligente seria:
print('A soma ente {} e {} vale {}'.format(N1, N2, S))
