# Criando uma cópia de uma lista:

Original = list()
Original.append('André')
Original.append(20)

Copia = []

Copia.append(Original[:])           # Copia

Original[0] = 'Maria'
Original[1] = 30

Copia.append(Original[:])

print(Original)
print(Copia)
