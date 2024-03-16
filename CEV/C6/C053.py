# Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

A1 = input('Digite uma frase: ').upper().strip()

A2 = A1.split()

T = ''.join(A2)

I = ''

for L in range(len(T) -1, -1, -1):

    I += T[L]

print('O inverso de {} é {}'.format(A1,I))

if I == T:
    print('{} é um palíndromo!'.format(A1))

else:
    print('{} NÃO é um palíndromo!'.format(A1))




