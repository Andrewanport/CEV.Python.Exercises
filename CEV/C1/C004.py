# Exercício Python 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
# .

A = input('Digite qualquer coisa: ')
print('Isso é numérico?')
print(A.isnumeric())
print('Isso é alfabético?')
print(A.isalpha())
print('Isso é ASCII?')
print(A.isascii())
print('Isso é um dígito?')
print(A.isdigit())