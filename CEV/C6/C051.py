# Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
# .

print('-'*23)
print('PROGRESSÃO ARITMÉTICA ')
print('-'*23)

P = int(input('Digite o início da PA: '))
R = int(input('Digite a razão da PA: '))
D = P + (10 - 1) * R

for c in range(P, D + R, R):
    print('{} '.format(c), end='⭢ ')

print(' FIM')


# ============ Other Option: ============ #

n = int(input('Informe o primeiro termo da PA: '))
r = int(input('Digite a razão: '))
for c in range(1,11):
    pa = n + r * c
    print(pa, end=' ⭢ ')

print(' FIM')

quit()
