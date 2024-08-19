
temp = []
main = []
heavy = []
light = []

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))

    if len(main) == 0:
        heavy = light = temp[1]

    else:
        if temp[1] > heavy:
            heavy = temp[1]
        if temp[1] < light:
            light = temp[1]

    main.append(temp[:])
    temp.clear()

    answer = str(input('Quer continuar? [S/N]')).upper()

    if answer == 'N':
        break

print(f'| Número de pessoas cadsatradas: {len(main)}')

print(f'| O maior peso foi de: {heavy}Kg', end=' ')
for p in main:
        if p[1] == heavy:
            print(f'[{p[0]}]', end=' ')

print(f'\n| O menor peso foi de {light}Kg', end=' ')
for p in main:
        if p[1] == light:
            print(f'[{p[0]}]', end=' ')
