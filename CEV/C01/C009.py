# Exercício Python 009: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
# .

N = int(input('Digite um número: '))

# Estética
print('-'*25)

# Tabuada
print('{} x {} = {}'.format(N, 1, N*1))
print('{} x {} = {}'.format(N, 2, N*2))
print('{} x {} = {}'.format(N, 3, N*3))
print('{} x {} = {}'.format(N, 4, N*4))
print('{} x {} = {}'.format(N, 5, N*5))
print('{} x {} = {}'.format(N, 6, N*6))
print('{} x {} = {}'.format(N, 7, N*7))
print('{} x {} = {}'.format(N, 8, N*8))
print('{} x {} = {}'.format(N, 9, N*9))
print('{} x {} = {}'.format(N, 10, N*10))

# Estética
print('-'*25)

# Utilizar \n não seria uma boa solução aqui pois devemos considerar a legibilidade do código!
# Perceba como ficaria mais poluído:

#print('{} x 1 = {}\n'
#      '{} x 2 = {}\n'
#      '{} x 3 = {}\n'
#      '{} x 4 = {}\n'
#      '{} x 5 = {}\n'
#      '{} x 6 = {}\n'
#      '{} x 7 = {}\n'
#      '{} x 8 = {}\n'
#      '{} x 9 = {}\n'
#      '{} x 10 = {}'.format(N,N*1,N,N*2,N,N*3,N,N*4,N,N*5,N,N*6,N,N*7,N,N*8,N,N*9,N,N*10))