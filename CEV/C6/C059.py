"""

Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.

"""

O = 0

# Main While
while O != 5:

    # Inputs
    N1 = float(input('Digite um número (1): '))
    N2 = float(input('Digite um número (2): '))

    # Main Print
    print('[1] Soma'
          '\n[2] Multiplicação'
          '\n[3] Maior'
          '\n[4] Novos Números'
          '\n[5] Sair do programa')

    # Option input
    O = int(input('Selecione uma opção: '))

    # Operations
    S = N1 + N2
    M = N1 * N2

    # Conditional (1)
    if O == 1:
        print('A SOMA ente {} e {} é de: {}'.format(N1, N2, S))
        quit()

    # Conditional (2)
    elif O == 2:
        print('A MULTIPLICAÇÃO ente {} e {} é de: {}'.format(N1, N2, M))
        quit()

    # Conditional (3)
    elif O == 3:
        if N1 > N2:
            print('O Número {} é maior que {}'.format(N1, N2))
            quit()
        elif N1 < N2:
            print('O Número {} é maior que {}'.format(N2, N1))
            quit()
        else:
            print('Os Números {} e {} são iguais'.format(N1, N2))
            quit()

    # Conditional (4)
    elif O == 4:
        print('Informe os número novamente! ')

    # Conditional (5)
    elif O == 5:
        print('Programa encerrado!')
        quit()

    else:
        print('opção inválida!')
