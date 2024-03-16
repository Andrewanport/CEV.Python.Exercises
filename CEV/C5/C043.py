# Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

P = float(input('Digite seu peso (Kg): '))
A = float(input('Digite sua altura (m): '))

IMC = P / (A**2)

if IMC < 18.5:
    print('IMC: {}'.format(IMC))
    print('Situação: ABAIXO DO IDEAL')

elif 18.5 <= IMC < 25:
    print('IMC: {}'.format(IMC))
    print('Situação: IDEAL')

elif 25 <= IMC < 30:
    print('IMC: {}'.format(IMC))
    print('Situação: ACIMA DO IDEAL (1)')

elif 30 <= IMC < 40:
    print('IMC: {}'.format(IMC))
    print('Situação: ACIMA DO IDEAL (2)')

elif IMC > 40:
    print('IMC: {}'.format(IMC))
    print('Situação: ACIMA DO IDEAL (3)')
