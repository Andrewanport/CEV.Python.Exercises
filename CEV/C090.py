"""""
Exercício Python 090: 
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
No final, mostre o conteúdo da estrutura na tela.
"""""

Aluno = dict()

Aluno['Nome'] = str(input('Digite o nome do aluno: '))
Aluno['Média'] = float(input(f'Digite a média do aluno {Aluno['Nome']}: '))

if Aluno['Média'] >= 7:
    Aluno['Situação'] = '\033[1;32mAprovado\033[m'

elif 5 <= Aluno['Média'] < 7:
    Aluno['Situação'] = '\033[1;33mRecuperação\033[m'

else:
    Aluno['Situação'] = '\033[1;31mReprovado\033[m'

print(15 * '<>')
for k, v in Aluno.items():
    print(f'{k} do aluno: {v}')
print(15 * '<>')

quit()
