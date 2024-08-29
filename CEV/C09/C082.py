"""""
Exercício Python 082: 
Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
Ao final, mostre o conteúdo das três listas geradas.
"""""

L = []          # Or:   L = list()
P = []          # Or:   P = list()
I = []          # Or:   I = list()

R = 'S'

while R == 'S':

    N = int(input('Digite um valor inteiro: '))
    L.append(N)

    if N % 2 == 0:
        P.append(N)
        print(f'Valor adicionado à lista \033[1;36mPAR\033[m')
        R = str(input('Deseja continuar? [S/N]: ')).upper()

    else:
        I.append(N)
        print(f'Valor adicionado à lista \033[1;36mÍMPAR\033[m')
        R = str(input('Deseja continuar? [S/N]: ')).upper()

print(f'Números digitados {L}')
print(f'Números \033[1;36mPARES\033[m {P}')
print(f'Números \033[1;36mÍMPARES\033[m {I}')