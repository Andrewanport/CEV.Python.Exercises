"""

Exercício Python 061:
Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.

"""

print('-'*23)
print('PROGRESSÃO ARITMÉTICA ')
print('-'*23)

P = int(input('Digite o início da PA: '))
R = int(input('Digite a razão da PA: '))
D = P + (10 - 1) * R

T = P

C = 1

while C <= 10:
    print('{} '.format(T), end='⭢ ')
    T += R
    C += 1

print(' FIM')



