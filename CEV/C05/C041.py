# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

from datetime import date

A = date.today().year

N = int(input('Digite o ano em que nasceu: '))

I = A - N

if I <= 9:
    print('Idade: {} ano(s)'.format(I))
    print('Classificação: MIRIM')
    quit()

elif I <= 14:
    print('Idade: {} ano(s)'.format(I))
    print('Classificação: INFANTIL')
    quit()

elif I <= 25:
    print('Idade: {} ano(s)'.format(I))
    print('Classificação: SÊNIOR')
    quit()

elif I > 25:
    print('Idade: {} ano(s)'.format(I))
    print('Classificação: MASTER')
    quit()