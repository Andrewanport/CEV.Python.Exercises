# Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

A = date.today().year

# Counters
MA = 0          # MA = Maiores de idade
ME = 0          # ME = Menores de idade

for i in range(1, 8):

    N = int(input('Digite o ano em que a {}ª pessoa nasceu: '.format(i)))

    if A - N >= 18:
        MA += 1

    else:
        ME += 1

print('{} pessoas são MENORES de idade!'.format(ME))
print('{} pessoas são MAIORES de idade!'.format(MA))



