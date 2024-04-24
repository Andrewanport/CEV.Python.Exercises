"""""
Exercício Python 077:
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""""

T = ('EU', 'SOU', 'O', 'SENHOR', 'CHAMPIONS')

V = ('A', 'E', 'I', 'O', 'U')

for p in T:
    print(f'\n\033[mPalavra: \033[1;32m{p} \033[m| Vogais:\033[1;32m ', end='')

    for letra in p:
        if letra.upper() in 'AEIOU':
            print(letra, end=' ')
