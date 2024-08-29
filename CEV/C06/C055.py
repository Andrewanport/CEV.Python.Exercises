# Exercício Python 055: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

# Counters

MA = 0          # MA = Maior Peso
ME = 0          # ME = Menor Peso
ALL = 0         # MED = Média

for i in range(1, 6):
    P = float(input('Digite o peso da {}ª pessoa: '.format(i)))

    # Somatório:
    ALL += P

    # Média:
    MED = ALL / i

    # Condicionais:

    # Se for a primeira ocorrência, ele será tanto o maior quanto o menor
    if i == 1:
        MA = P
        ME = P

    else:
        if P > MA:
            MA = P

        elif P < ME:
            ME = P

print('O MAIOR peso registrado foi de: {}Kg'.format(MA))
print('O MENOR peso registrado foi de: {}Kg'.format(ME))
print('A SOMA de todos os pesos foi de: {}Kg'.format(ALL))
print('A MÉDIA de peso foi de: {}Kg'.format(MED))






# =================== Other way =================== #

List = []       # Empty list

for i in range(1, 6):

    P = float(input('Digite o peso da {}ª pessoa: '.format(i)))

    List += [P]     # add valores de peso

print('O MAIOR peso registrado foi de: {}Kg'.format(max(List)))     # Valor máximo encontrado na lista
print('O MENOR peso registrado foi de: {}Kg'.format(min(List)))     # Valor mínimo encontrado na lista
