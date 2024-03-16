# Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
# .

from random import choice

A1 = input('Digite o nome de um aluno (1): ')
A2 = input('Digite o nome de um aluno (2): ')
A3 = input('Digite o nome de um aluno (3): ')
A4 = input('Digite o nome de um aluno (4): ')

L = [A1,A2,A3,A4]
C = choice(L)

print('O aluno sorteado foi {} !'.format(C))
