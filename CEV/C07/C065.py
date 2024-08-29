"""
Exercício Python 065:
Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""

# Resposta do usuário
R = 'S'

# Soma
S = 0

# Maior
MA = 0

# Menor
ME = 0

# Média
MED = 0

# Quantidade
Q = 0

while R == 'S':
    N = int(input('Digite um número: '))
    R = str(input('Deseja continuar? [S/N]: ')).upper()

    # Soma
    S += N

    # Quantidade
    Q += 1

    # Primeira instância
    if Q == 1:
        MA = N
        ME = N

    else:
        if N > MA:
            MA = N

        if N < ME:
            ME = N

# Média
MED = S/Q

# Outputs
print('\033[1;32mA média d valor digitado foi {}'.format(MED))
print('\033[1;32mO maior valor digitado foi {} e o menor {}'.format(MA, ME))
