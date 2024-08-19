Galera = []
dado = []

Count = 1

TMaiorI = TMenorI = 0

for c in range(0, 3):
    dado.append(str(input('Digite o nome ({}): '.format(Count))))
    dado.append(int(input('Digite a idade ({}): '.format(Count))))
    Count += 1

    Galera.append(dado[:])              # Cria uma cópia de dado
    dado.clear()

for p in Galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
        TMaiorI += 1

    else:
        print(f'{p[0]} é menor de idade')
        TMenorI += 1

print(f'Temos {TMaiorI} maiores e {TMenorI} menores de idade')