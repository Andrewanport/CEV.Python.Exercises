# Faça um programa que leia um número de 0 a 9999 e mostre na tela um dos dígitos separados
# .

N = input(('Digite um número de quatro dígitos: '))

print('Seu número é: {}'.format(N))
print('A unidade do número {} é: {}'.format(N, N[3]))
print('A dezena do número {} é: {}'.format(N, N[2]))
print('A centena do número {} é: {}'.format(N, N[1]))
print('A milhar do número {} é: {}'.format(N, N[0]))

# ----------------- Outra forma: ------------------ #

N = int(input(('Digite um número de quatro dígitos: ')))

U = N // 1 % 10
D = N // 10 % 10
C = N // 100 % 10
M = N // 1000 % 10

print('Seu número é: {}'.format(N))
print('A unidade do número {} é: {}'.format(N, U))
print('A dezena do número {} é: {}'.format(N, D))
print('A centena do número {} é: {}'.format(N, C))
print('A milhar do número {} é: {}'.format(N, M))