"""""
Exercício Python 071: 
Crie um programa que simule o funcionamento de um caixa eletrônico. 
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) 
e o programa vai informar quantas cédulas de cada valor serão entregues.

OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""""

print('\033[33m<>'*14)
print("       ANDREW'S BANK")
print('\033[33m<>\033[m'*14)

T = 0

S = 0

while S <= 0:
    S = int(input('Digite o valor que deseja sacar: R$'))

NC = 0
NV = 0
ND = 0
NU = 0

while True:

    while S >= 50:
        # Number of 50
        NC += 1
        S -= 50

    while S >= 20:
        # Number of 20
        NV += 1
        S -= 20

    while S >= 10:
        # Number of 10
        ND += 1
        S -= 10

    while S >= 1:
        # Number of 1
        NU += 1
        S -= 1

    if S == 0:
        break

print(f'\033[33m{NC} \033[0mcédulas de \033[33mR$50')
print(f'\033[33m{NV} \033[0mcédulas de \033[33mR$20')
print(f'\033[33m{ND} \033[0mcédulas de \033[33mR$10')
print(f'\033[33m{NU} \033[0mcédulas de \033[33mR$1')
