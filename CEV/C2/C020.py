# Exercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
# .

import random

A1 = input('Digite o nome do aluno (1): ')
A2 = input('Digite o nome do aluno (2): ')
A3 = input('Digite o nome do aluno (3): ')
A4 = input('Digite o nome do aluno (4): ')

# array
L = [A1, A2, A3, A4]

# Misturada aleatória
random.shuffle(L)

print('A ordem de apresentação dos alunos é: {}'.format(L))