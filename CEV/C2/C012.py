# Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
# .

I = int(input('Digite o código do produto: '))
P = (float(input('Digite o valor original do produto de código {}: '.format(I))))

B = P - (P * 15/100)

# Também poderíamos atribuir ao desconto, se for de 5%, a seguinte operação:
#B = P * 0.95

print('Código do produto: {}\n'
      'Valor original: R${}\n'
      'Valor em blackfriday: R${}'.format(I,P,B))

