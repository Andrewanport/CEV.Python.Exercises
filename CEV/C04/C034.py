# Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários inferiores a R$5000,00, calcule um aumento de 15%.
# Valores que variam entre 5000 e 10000, o aumento é de 10%.
# Valores superiores à 10000, o aumento é de 5%.
# .

S = float(input('Digite o salário atual deste funcionário: '))
print('-'*50)

if S < 1412:

    print('O salário mínimo é de R$ 1.412.')
    print('Selecione um valor válido.')

if 1412 <= S <= 5000:

    R = S + (S * 0.15)
    A = S * 0.15

    print('Salário atual: {:.2f}'.format(S))
    print('Valor do aumento: {:.2f}'.format(A))
    print('Novo salário: {:.2f}'.format(R))

if 5000 <= S <= 10000:

    R = S + (S * 0.10)
    A = S * 0.10

    print('Salário atual: {:.2f}'.format(S))
    print('Valor do aumento: {:.2f}'.format(A))
    print('Novo salário: {:.2f}'.format(R))

if S > 10000:

    R = S + (S * 0.05)
    A = S * 0.05

    print('Salário atual: {:.2f}'.format(S))
    print('Valor do aumento: {:.2f}'.format(A))
    print('Novo salário: {:.2f}'.format(R))
