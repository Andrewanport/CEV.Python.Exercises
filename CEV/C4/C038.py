# Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

N1 = int(input('Digite um número (1): '))
N2 = int(input('Digite um número (2): '))

if N1 > N2:
    print('{} é maior que {}'.format(N1,N2))

elif N2 > N1:
    print('{} é maior que {}'.format(N2,N1))

elif N1 == N2:
    print('{} é igual à {}'.format(N1,N2))