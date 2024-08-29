"""
Exercício Python 067:
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.
"""

while True:

    # Input
    N = int(input('Digite um número inteiro: '))

    # Flag
    if N < 0:
        print('Programa Finalizado!')
        break

    # Reiniciar valor da variável
    C = 0

    while C < 11:

        # Operação
        M = N * C

        # Output
        print(f'|{N:2} x {C:2} = {M:2} |')

        # Increment
        C += 1
