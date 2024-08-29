# Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

L1 = float(input('Digite o valor da medida (1): '))
L2 = float(input('Digite o valor da medida (2): '))
L3 = float(input('Digite o valor da medida (3): '))

if L1 < L2 + L3 and L2 < L1 + L3 and L3 < L1 + L2:

    print('\033[1;32mFORMAM um triângulo.'.format(L1, L2, L3))

    if L1 == L2 == L3:
        print('Valores: {:.2f}, {:.2f}, {:.2f}'.format(L1, L2, L3))
        print('Triângulo: EQUILÁTERO')
        quit()

    elif L1 == L2 != L3 or L2 == L3 != L1 or L1 == L3 != L2:
        print('Valores: {:.2f}, {:.2f}, {:.2f}'.format(L1, L2, L3))
        print('Triângulo: ISÓCELES')
        quit()

    elif L1 != L2 != L3:
        print('Valores: {:.2f}, {:.2f}, {:.2f}'.format(L1, L2, L3))
        print('Triângulo: ESCALENO')
        quit()

else:
    print('\033[1;31mOs valores {}, {} e {}, NÃO FORMAM um triângulo'.format(L1, L2, L3))
    quit()
