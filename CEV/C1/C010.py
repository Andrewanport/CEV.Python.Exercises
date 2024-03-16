# Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere: US$ 1.00 = R$ 4.93
#.

R = float(input('Quantos reais você tem em sua carteira? '))

D = R / 4.93

print('Com o valor de {} reais, você tem o equivalente à {:.2f} doláres!'.format(R,D))
