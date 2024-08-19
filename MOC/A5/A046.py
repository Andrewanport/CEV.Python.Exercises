
Lanche = ['Sorvete', 'hamburguer', 'batata']

Lanche.append('Cookie')

print(Lanche)

Lanche.insert(2,'hotdog')

print(Lanche)

del Lanche[2]

print(Lanche)

Lanche.pop(0)

print(Lanche)

Lanche.remove('batata')

print(Lanche)

Lanche.pop()

print(Lanche)

if 'pizza' in Lanche:
    Lanche.remove('pizza')

else:
    print('sem pizza')

Lanche2 = ['Sorvete', 'hamburguer', 'batata', 'pizza', 'pipoca', 'chiclete']

Valores = list(range(2,6))

print(Valores)

numeros = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print(numeros)

numeros.sort()

print(numeros)

# Organiza de forma decrescente
numeros.sort(reverse=True)

print(numeros)

# Inverte a ordem dos termos (não necessariamente de forma organizada)
numeros.reverse()

print(numeros)

print(len(numeros))