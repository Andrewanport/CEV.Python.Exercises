"""""
Exercício Python 070: 
Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra. (T)
B) quantos produtos custam mais de R$1000. (C)
C) qual é o nome do produto mais barato.  (B)
"""""

print(15 * '<>')
print("       ANDREW'S STORE      ")
print(15 * '<>')

T = 0           # Total
C = 0           # Acima de 1000
B = None           # Valor Mais Barato
NB = ''         # Nome do mais barato
I = 0           # Número de itens


while True:
    N = str(input('Nome do produto: '))
    P = float(input('Preço: R$ '))

    # Sum
    T += P

    # Counter
    I += 1

    # Verifies the cheaper one
    if B is None or P < B:
        B = P
        NB = N

    if P > 1000:
        C += 1

    E = ' '

    while E not in 'SN':
        E = str(input('Mais produtos? [S/N]: ')).upper().strip()[0]

    if E == "N":
        break

print(10*'-', 'Fim', 10*'-')
print(f'Número de itens: {I}')
print(f'Valor total da compra: R${T}')
print(f'Número de produtos acima de R$1000: {C}')
print(f'Nome da produto mais barato (R${B}): {NB}')
