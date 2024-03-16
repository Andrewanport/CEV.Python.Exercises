# Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.
#.

# Acumulador
P = 0
I = 0

# Contador
SP = 0
SI = 0

for c in range(1, 7):
    A = int(input('Digite um número: '))

    if A % 2 == 0:
        P += A
        SP += 1

    elif A % 2 != 0:
        I += A
        SI += 1

print('Você forneceu {} números PARES. A soma desses números é:'.format(SP), '\033[1;34m{}\033[0m'.format(P))

print('Você forneceu {} números ÍMPARES. A soma desses números é:'.format(SI), '\033[1;34m{}'.format(I))


