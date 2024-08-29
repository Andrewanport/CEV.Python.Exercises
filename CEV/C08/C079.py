"""""
Exercício Python 079: 
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
Caso o número já exista lá dentro, ele não será adicionado. 
No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 
"""""

Lista = []

R = 'S'

while R == 'S':
    N = int(input('Digite um valor: '))

    if N in Lista:
        print('\033[1;31mNúmero duplicado!\033[m O valor não pôde ser adicionado!')
        R = str(input('Deseja continuar? [S/N]: ')).upper()

    else:
        Lista.append(N)
        print('\033[1;32mNúmero adicionado com sucesso!\033[m')
        R = str(input('Deseja continuar? [S/N]: ')).upper()

print(f'Os valores digitados foram: {sorted(Lista)}')
