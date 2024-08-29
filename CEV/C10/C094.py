"""""
Exercício Python 094: 
Crie um programa que leia nome, sexo e idade de várias pessoas, 
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
"""""

Group = list()
Individual = dict()
Sum = 0
Average = 0

while True:
    Individual.clear()
    Individual['Nome'] = str(input('Nome: '))
    while True:
        Individual['Sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if Individual['Sexo'] in 'MF':
            break
        print('Incorreto, responda apenas com [M/F].')
    Individual['Idade'] = int(input('Idade: '))
    Sum += Individual['Idade']
    Group.append(Individual.copy())

    while True:
        R = str(input('Deseja continuar? [S/N]: ')).upper()[0]
        if R in 'SN':
            break
        print('Incorreto, responda apenas com [S/N]')
    if R == 'N':
        break

print(30 * '~~')

print(f'1. Número de pessoas: {len(Group)}')

print(30 * '~~')

Average = Sum / len(Group)
print(f'2. Média de idade do grupo: {Average:5.2f} anos')

print(30 * '~~')

print(f'3. As mulheres cadastradas foram: ', end='')

for p in Group:
    if p['Sexo'] in 'Ff':
        print(f'{p["Nome"]} ', end='')
print()

print(30 * '~~')

print('4. Lista de pessoas que estão acima da média: ')

for p in Group:
    if p['Idade'] >= Average:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()

print(30 * '~~')

