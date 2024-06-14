"""""
Exercício Python 085: 
Crie um programa onde o usuário possa digitar sete valores numéricos 
e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
No final, mostre os valores pares e ímpares em ordem crescente.
"""""

tot = [[], []]

c = 1
for i in range(1, 8):
    N = int(input(f'Digite um valor inteiro ({c}ª): '))
    c += 1

    if N % 2 == 0:
        tot[0].append(N)

    if N % 2 != 0:
        tot[1].append(N)

print(f'Os valores PARES são: \033[1;32m{sorted(tot[0])}\033[m')
print(f'Os valores ÍMPARES são: \033[1;32m{sorted(tot[1])}\033[m')

print(tot)