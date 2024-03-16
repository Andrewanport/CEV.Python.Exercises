# Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

N = int(input('Digite um número inteiro: '))

C = int(input('Digite a opção que deseja: '            # Também poderia fazer com 3 aspas simples ''' caso desejasse não usar o \n
              '\n[1] Converter para BINÁRIO.'
              '\n[2] Converter para OCTAL'
              '\n[3] Converter para HEXADECIMAL'
              '\nSua escolha: '
              ))

if C == 1:
    R = bin(N)
    print('{} convertido para BINÁRIO, é: {}'.format(N,R[2:]))

elif C == 2:
    R = oct(N)
    print('{} convertido para OCTAL, é: {}'.format(N, R[2:]))

elif C == 3:
    R = hex(N)
    print('{} convertido para HEXADECIMAL, é: {}'.format(N, R[2:]))

else:
    print('Opção inválida, tente novamente!')