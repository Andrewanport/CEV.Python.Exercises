# Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
# .
N = int(input('Digite um número: '))

print('O dobro de {} é: {} \n'
      'O triplo de {} é: {} \n'
      'A raiz quadrada de {} é: {:.3f} '.format(N, N*2, N, N*3, N, N**1/2))