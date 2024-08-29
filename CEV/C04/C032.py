# Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
# .

A = int(input('Qual ano deseja avaliar? Digite 0 para o ano atual. '))

if A % 4 == 0 and A % 100 != 0 or A % 400 == 0:
    print('{} é um ano bissexto'.format(A))

else:
    print('{} Não é um ano bissexto'.format(A))