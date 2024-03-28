"""
Exercício Python 049:
Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
"""

N = int(input('Digite um número: '))

if N == 0:
    print('\033[1;32mQualquer valor multiplicado por 0 é igual à 0')
    quit()

elif N != 0:

    print('-'*25)

    for c in range(1, 21):

        print('{} x {:2} = {}'.format(N, c, N * c))

    print('-' * 25)
    quit()