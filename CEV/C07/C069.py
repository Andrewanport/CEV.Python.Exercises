"""
Exercício Python 069:
Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos. (x)
B) quantos homens foram cadastrados. (y)
C) quantas mulheres tem menos de 20 anos. (z)
"""

# Counters
X = 0
Y = 0
Z = 0

# Intro
print(30 * '-')
print('CADASTRE UM CLIENTE')
print(30 * '-')

while True:

    # Initialise
    S = ' '
    I = 0

    # Verifies
    while I <= 0:
        I = int(input('Idade: '))

    # Verifies
    while S not in 'MF':
        S = str(input('Sexo [M/F]: ')).upper().strip()[0]

    print(30 * '-')

    # Counter x
    if I >= 18:
        X += 1

    # Counter Y
    if S == 'M':
        Y += 1

    # Counter Z
    if S == 'F' and I < 20:
        Z += 1

    E = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    print(30 * '-')

    # Flag
    if E == 'N':
        break

print(f'Número de clientes maiores de idade: {X}')
print(f'Número de clientes do sexo masculino: {Y}')
print(f'Número de clientes do sexo feminino menores de 20 anos: {Z}')
