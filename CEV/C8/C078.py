"""""
Exercício Python 078: 
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 
"""""

Lista = []

for i in range(0, 5):
    Lista.append(int(input('Digite um valor inteiro: ')))

Maior = max(Lista)
Menor = min(Lista)

print(f'Os valores digitados foram: {Lista}')

print(f'Maior número: {max(Lista)} | {Lista.index(Maior) + 1}ª posição')

print(f'Menor número: {min(Lista)} | {Lista.index(Menor) + 1}ª posição ')