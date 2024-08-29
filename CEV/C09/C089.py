"""""
Exercício Python 089: 
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""""

ficha = []

while True:
    name = str(input('Name: '))
    G1 = float(input('Grade (1): '))
    G2 = float(input('Grade (2): '))
    Average = ((G1 + G2) / 2)
    ficha.append([name, [G1, G2,], Average])
    answer = str(input('Keep going? [Y/N]: ')).upper()

    if answer == 'N':
        break

print(f'{"Num.":4<}{"Name":<10}{"Average":>8}')

for i, a in enumerate(ficha):
    print(f'{i + 1:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print(50*'-')
    opt = int(input("Who's grade you wanna see? (-1 to stop): "))
    if opt == -1:
        break

    if opt <= len(ficha) - 1:
        print(f"{ficha[opt][0]}'s grades are: {ficha[opt][1]}")
print(50*'-')

