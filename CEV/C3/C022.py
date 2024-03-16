# Crie um programa que leia o nome completo de uma pessoa e mostra:
# O nome com todas as letras maiúsculas
# O nome com todas as letras minúsculas
# Quantas letras ao sem considerar espaços.
# Quantas letras tem o primeiro nome?
# .

N = input('Digite o seu nome completo (3 nomes): ')

print('Seu nome completo é: {}'.format(N))

print('Seu nome completo (maiúsculo) é: {}'.format(N.upper()))

print('Seu nome completo (minúsculo) é: {}'.format(N.lower()))

print('Seu nome completo tem: {} letras'.format(len(N)-N.count(' ')))

print('Seu primeiro nome tem: {} letras'.format(N.find(' ')))

S = N.split()

print('Seus nomes são: {}'.format(S))

print('Seu nome (1) é: {}'.format(S[0], len(S)))
print('Seu nome (2) é: {}'.format(S[1], len(S)))
print('Seu nome (3) é: {}'.format(S[2], len(S)))

