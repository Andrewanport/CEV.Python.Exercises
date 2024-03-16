# Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
# .

S1 = float(input('Digite um segmento (1): '))
S2 = float(input('Digite um segmento (2): '))
S3 = float(input('Digite um segmento (3): '))

if S1 < S2 + S3 and S2 < S1 + S3 and S3 < S1 + S2:
    print('\033[1;32mOs valores {}, {} e {}, FORMAM um triângulo.'.format(S1, S2, S3))

else:
    print('\033[1;31mOs valores {}, {} e {}, NÃO FORMAM um triângulo'.format(S1, S2, S3))