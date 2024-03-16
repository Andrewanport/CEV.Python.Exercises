# Exercício Python 008: Escreva um programa que leia um valor em metros e o
# exiba convertido em centímetros e milímetros.
# .

M = float(input('Digite um valor em metros: '))

C = M * 100
MM = M * 1000

print('O valor {} em metros, equivale à: {:.2f} em centímetros \n'
      'O valor {} em metros, equivale à: {:.2f} em milímetros'.format(M,C,M,MM))