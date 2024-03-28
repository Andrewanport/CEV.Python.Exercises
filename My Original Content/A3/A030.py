
# Counters
I = 0
P = 0
NEG = 0
C = 0

R = 'S'

while R == 'S':

    C += 1

    N = int(input('Digite um número ({}): '.format(C)))
    R = str(input('Deseja continuar? [S/N]: ')).upper()

    if N % 2 == 0:
        P += 1

    if N % 2 != 0:
        I += 1

    if N < 0:
        NEG += 1

print('Você digitou {} números pares'.format(P))
print('Você digitou {} números ímpares'.format(I))
print('Você digitou {} números negativos'.format(NEG))
