# Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário
# e mostre seu novo salário, com 15% de aumento.

F = input('Nome do funcionário: ')
S = float(input('Salário atual do funcionário {} : '.format(F)))

A = S + (S * 15 / 100)

# Também poderíamos atribuir ao aumento, se for de 15%, a seguinte operação:
#A = S * 1.15

print('O funcionário {} recebia o valor de R${:.2f}\n'
      'Agora, recebe à o equivalente à R${:.2f}'.format(F,S,A))