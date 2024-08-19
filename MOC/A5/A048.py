
Valores = []

Valores.append(4)
Valores.append(5)
Valores.append(6)
Valores.append(7)

print(Valores)

for c, v in enumerate(Valores):
    print(f'{v} | ', end='')

for c, v in enumerate(Valores):
    print(f'\nNa posição {c} encontrei o valor {v} | ', end='')

print('\nFim da lista 1')

Valores2 = []

for count in range(0, 4):
    Valores2.append(int(input('Digite um valor: ')))

for c, v in enumerate(Valores2):
    print(f'\nNa posição {c} encontrei o valor {v} | ', end='')