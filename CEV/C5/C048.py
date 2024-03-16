# Exercício Python 048: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
# .

S = 0
T = 0

for c in range (1, 501, 2):
    if c % 3 == 0:
        S += c
        T += 1

print('\033[1;32mA soma dos valores múltiplos de 3, de 0 à 500 é: {}'.format(S))
print('\033[1;32m{} números foram solicitados!'.format(T))