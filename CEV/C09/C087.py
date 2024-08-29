"""""
Exercício Python 087: 
Aprimore o desafio anterior, mostrando no final: 

A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
"""""

mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

sp = c3 = 0

for l in range(0, 3):
    for c in range(0, 3):
        N = mat[l][c] = int(input(f' Digite um valor para [{l} x {c}]: '))

        if N % 2 == 0:
            sp += N

for l in range(0, 3):
    c3 += mat[l][2]

for l in range(0, 3):
    for c in range(0, 3):
        print(f' [{mat[l][c]:^5}]', end='')
    print()

print(f'Soma dos valores pares da matriz: {sp}')
print(f'soma dos valores da terceira coluna: {c3}')
print(f'O maior valor da segunda linha: {max(mat[1])}')
