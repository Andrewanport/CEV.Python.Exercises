"""""
Exercício Python 077:
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""""

T = ('EU', 'SOU', 'O', 'SENHOR', 'CHAMPIONS')

V = ('A', 'E', 'I', 'O', 'U')

for i in T:
    for letra in i:
        if letra in V:
            print(f'O caractere "{letra}" | \033[1;32mÉ uma vogal\033[m')
        else:
            print(f'O caractere "{letra}" | \033[1;31mNÃO é uma vogal\033[m')
