"""""
Exercício Python 074: 
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""""

from random import randint

N = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))

print(f'Os números sorteados foram: {N}')

print(f'A ordem crescente dos números é: {sorted(N)}')

Maior = sorted(N)[4]
print(f'O maior número é {Maior}')

Menor = sorted(N)[0]
print(f'O menor número é {Menor}')

print(f'A soma dos valores sorteados é de: {sum(N)}')