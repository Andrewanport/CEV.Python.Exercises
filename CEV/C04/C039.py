# Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
# .

from datetime import date

N = int(input('Digite seu ano de Nascimento: '))

A = date.today().year

I = A - N

if I < 18:
    print('Você tem {} anos.'.format(I))
    print('{} será o ano do seu alistamento.'.format(N + 18))
    print('Situação: Antecipado')
    quit()

elif I == 18:
    print('Você tem {} anos.'.format(I))
    print('{} é o ano do seu alistamento.'.format(N + 18))
    print('Situação: Regular')
    quit()

elif I > 18:
    print('Você tem {} anos.'.format(I))
    print('{} foi o ano do seu alistamento.'.format(N + 18))
    print('Situação: Atrasado')
    quit()