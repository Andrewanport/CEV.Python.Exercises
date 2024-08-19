
a = [2, 3, 4, 7]
b = a

print(f'Lista A: {a}')
print(f'Lista B: {b}')

b[2] = 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')

# Quando você está fazendo com que uma lista receba [=] uma outra lista vc está conectando elas, por tanto uma alteração modifica ambas listas

c = [2, 3, 4, 7]
d = c[:]            # Criando uma cópia da lista c

d[2] = 8

print(f'Lista C: {c}')
print(f'Lista D: {d}')

# Nesse caso, não há ligação entre as duas listas, portanto são listas independentes