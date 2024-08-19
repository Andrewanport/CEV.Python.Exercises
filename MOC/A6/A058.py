"""""
Exercício Python 086: 
Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. 
No final, mostre a matriz na tela, com a formatação correta.
"""""

mat = [[[], [], []], [[], [], []], [[], [], []]]
c = 0
for i in range(0, 3):
    N = int(input('Digite um valor inteiro: '))
    mat[0][c].append(N)
    c += 1

c = 0
for i in range(0, 3):
    N = int(input('Digite um valor inteiro: '))
    mat[1][c].append(N)
    c += 1

c = 0
for i in range(0, 3):
    N = int(input('Digite um valor inteiro: '))
    mat[2][c].append(N)
    c += 1


print(f'{mat[0][0]} {mat[0][1]} {mat[0][2]}')
print(f'{mat[1][0]} {mat[1][1]} {mat[1][2]}')
print(f'{mat[2][0]} {mat[2][1]} {mat[2][2]}')

# -------------------------------- or -------------------------------- #

mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        mat[l][c] = int(input(f' Digite um valor para [{l} x {c}]: '))

print(f'[{mat[0][0]:^5}] [{mat[0][1]:^5}] [{mat[0][2]:^5}]')
print(f'[{mat[1][0]:^5}] [{mat[1][1]:^5}] [{mat[1][2]:^5}]')
print(f'[{mat[2][0]:^5}] [{mat[2][1]:^5}] [{mat[2][2]:^5}]')