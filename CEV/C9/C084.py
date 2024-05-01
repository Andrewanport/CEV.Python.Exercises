"""""
Exercício Python 084: 
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""""

# Lists:
temp = []
main = []
heavy = []
light = []

# Input loop:
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))

    # First input?
    if len(main) == 0:
        heavy = light = temp[1]

    # Update:
    else:
        if temp[1] > heavy:
            heavy = temp[1]     # [Heavy]

        if temp[1] < light:
            light = temp[1]     # [light]

    # Add inputs to main list
    main.append(temp[:])

    # Clears for next usage
    temp.clear()

    # More users?
    answer = str(input('Quer continuar? [S/N]')).upper()

    # Break
    if answer == 'N':
        break


print(f'| Número de pessoas cadsatradas: {len(main)}')

print(f'| O maior peso foi de: {heavy}Kg', end=' ')

# finding
for p in main:
    if p[1] == heavy:
        print(f'[{p[0]}]', end=' ')

print(f'\n| O menor peso foi de {light}Kg', end=' ')
for p in main:
    if p[1] == light:
        print(f'[{p[0]}]', end=' ')


