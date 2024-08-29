"""""
Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""""

from datetime import datetime

dados = dict()

dados['Nome'] = str(input('Nome: '))

Nascimento = int(input('Ano de nascimento: '))
dados['Idade'] = datetime.now().year - Nascimento

dados['Carteira de trabalho'] = int(input('Carteira de trabalho (0 = não tem): '))

if dados['Carteira de trabalho'] != 0:
    dados['Ano de contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: R$'))
    dados['Ano de aposentadoria'] = dados['Ano de contratação'] + 35
    dados['Idade de aposentadoria'] = dados['Idade'] + ((dados['Ano de contratação'] + 35) - datetime.now().year)

print(20 * '~~')
for k, v in dados.items():
    print(f' - {k} -> {v}')
