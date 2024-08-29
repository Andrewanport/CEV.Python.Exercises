"""""
Exercício Python 075: 
Desenvolva um programa que leia 4 valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""""

N = (int(input('Digite um número inteiro (1): ')),
     int(input('Digite um número inteiro (2): ')),
     int(input('Digite um número inteiro (3): ')),
     int(input('Digite um número inteiro (4): ')))

print(f'Você digitou os valores: {N}')

print(f'O número 9 apareceu {N.count(9)} vez(es)')

if 3 in N:
    print(f'O número 3 apareceu na {(N.index(3)) + 1}ª posição ')

else:
    print('O valor 3 não foi digitado')

print(f'Número(s) par(es): ', end='')

for P in range(0, 4):
    if N[P] % 2 == 0:

        print(N[P], end=' | ')
        P += 1
