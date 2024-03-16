# Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
# Considere que cada litro de tinta pinta uma área de 2m².

H = float(input('Qual a altura da sua parede (em metros)? '))
L = float(input('Qual a largura da sua parede (em metros)? '))

A = H * L

T = A / 2

print('Uma parede de {}m x {}m possui uma área de {:.2f}m² \n'
      'Portanto, serão necessários {:.1f} litros de tinta'.format(H, L, A, T))

