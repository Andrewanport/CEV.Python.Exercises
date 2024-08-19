"""""
Exercício Python 085: 
Crie um programa onde o usuário possa digitar sete valores numéricos 
e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
No final, mostre os valores pares e ímpares em ordem crescente.
"""""

tot = list()
par = list()
imp = list()

tot.append(par)
tot.append(imp)

c = 1

while True:
    N = int(input(f'Digite um número inteiro ({c}º): '))
    c += 1

    if N % 2 == 0:
        par.append(N)

    if N % 2 != 0:
        imp.append(N)

    A = str(input('Deseja continuar? [S/N]: ')).upper()

    if A == 'N':
        break

print(f'Os valores PARES são: \033[1;32m{par}\033[m')
print(f'Os valores ÍMPARES são: \033[1;32m{imp}\033[m')

print(tot)
