"""""
Exercício Python 080: 
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
"""""

L = []
for i in range(0, 5):
    N = int(input('Digite um valor inteiro: '))

    if i == 0 or N > L[-1]:
        L.append(N)
    else:
        P = 0
        while P < len(L):
            if N <= L[P]:
                L.insert(P, N)
                break
            P += 1

print(f'A ordem dos valores é: {L}')