# Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre:
# a média de idade do grupo,
# qual é o nome do homem mais velho
# e quantas mulheres têm menos de 20 anos.

print('')

# Counters
MV = 0          # Mais Velho
MN = 0          # Mais Novo
SI = 0          # Soma da Idade
HV = ''         # Homem mais velho
MN20 = 0          # Mulheres novas

# Lists
Nomes = []
Idades = []
Sexos = []

for i in range(1, 5):

    # Main print
    print('----- {}ª Pessoa -----'.format(i))

    # Inputs
    N = str(input('Nome: ')).strip()
    I = int(input('Idade: '))
    S = str(input('Sexo (M/F): ')).strip().upper()

    # Soma Idades
    SI += I

    # Average
    Average = SI / i

    if i == 1 and S == 'M':
        MV = I
        HV = N

    if S == 'M' and I > MV:
        MV = I
        HV = N

    if S == 'F' and I <= 20:
        MN20 += 1


    # Add to lists
    Nomes += [N]
    Idades += [I]
    Sexos += [S]

print('A MAIOR de idade dos participantes foi de: {} anos, e pertence à {}, do sexo masculino! '.format(max(Idades), HV ))
print('A MÉDIA de idade dos participantes foi de: {} anos! '.format(Average))
print('{} mulheres possuem menos de 20 anos! '.format(MN20))

