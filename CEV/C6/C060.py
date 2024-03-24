"""

Exercício Python 060:
Faça um programa que leia um número qualquer e mostre o seu fatorial.

"""

from math import factorial

# Input
N = int(input('Digite um número para calcular seu fatorial: '))

# Counter
C = N

# Main operation
F = factorial(N)

# Main print
print('{}! = '.format(N), end='')

# Loop
while C > 0:
    print('{}'.format(C), end='')
    print(' x ' if C > 1 else ' = ', end='')

    # Counter modify
    C -= 1

print(' {}'.format(F),end='')

""" 

Também poderiamos fazer sem utilizar a propriedade factorial 

Bastaria iniciar a variável F em 1 

e incrementar no loop como: F *= C

"""


