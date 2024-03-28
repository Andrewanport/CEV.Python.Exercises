
# Exercicio 033 de forma mais otimizada e sem estrutura condicional

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite um último número: '))
A = [n1, n2, n3]
A.sort()
print(f'O maior número é {A[2]} e o menor é {A[0]}')