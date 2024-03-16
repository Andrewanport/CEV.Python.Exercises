# Exercício Python 005: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
# .

N = int(input('Digite um número: '))

print('O antecessor de {} é {} e o sucessor dele é {}'.format(N, N-1, N+1))