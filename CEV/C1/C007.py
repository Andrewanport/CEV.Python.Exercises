# Exercício Python 007: Desenvolva um programa que leia as duas notas de um aluno,
# calcule e mostre a sua média.
# .

Name = input('Digite o nome deo Aluno: ')

N1 = int(input('Digite uma nota (1): '))
N2 = int(input('Digite uma nota (2): '))
N3 = int(input('Digite uma nota (3): '))

M = (N1 + N2 + N3) / 3

print('A média do aluno {} é de {:.2f}'.format(Name, M))

