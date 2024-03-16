'''
Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''

R = str(input('Digite o seu sexo [M/F]: ')).upper()

if R == 'M' or R == 'F':
    print('Dados Cadastrados com sucesso!')
    quit()

else:
    while R != 'M' or R != 'F':
        R = str(input('Opção Inválida. Digite o seu sexo [M/F]: ')).upper()

        if R == 'M' or R == 'F':
            print('Dados Cadastrados com sucesso!')
            quit()

# ------------------------- Forma mais 'simples' -------------------------#

Sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]

while Sexo not in 'MmFf':
    Sexo = str(input('Opção Inválida. Digite o seu sexo [M/F]:'))

print('Dados Cadastrados com sucesso!')