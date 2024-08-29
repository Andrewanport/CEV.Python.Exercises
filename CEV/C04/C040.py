# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

N1 = float(input('Digite a sua nota (1): '))
N2 = float(input('Digite a sua nota (2): '))
N3 = float(input('Digite a sua nota (3): '))
N4 = float(input('Digite a sua nota (4): '))

M = (N1 + N2 + N3 + N4) / 4

if M < 5:
    print('Média: {:.2f}'.format(M))
    print('Situação: REPROVADO')
    quit()

elif 5 <= M <= 6.9:
    print('Média: {:.2f}'.format(M))
    print('Situação: RECUPERAÇÃO')
    quit()

elif M >= 7:
    print('Média: {:.2f}'.format(M))
    print('Situação: APROVADO')
    quit()