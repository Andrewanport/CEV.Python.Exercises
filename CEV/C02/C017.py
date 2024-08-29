# Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

import math

C1 = float(input('Digite a medida do cateto (1): '))
C2 = float(input('Digite a medida do cateto (2): '))

H = math.sqrt(C1**2 + C2**2)

print('O triângulo dos catetetos {:.2f} e {:.2f} possui uma hipotenusa de: {:.2f}'.format(C1, C2, H))
