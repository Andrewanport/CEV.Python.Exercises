# Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por KM rodado.

K = float(input('Quantos quilômetros (KM) o carro andou? '))
D = int(input('Por quantos dias o carro foi alugado? '))

Q = K * 0.15
T = D * 60

print('Distância percorrida: {:.2f}Km. Valor: R${:.2f}'.format(K, Q))
print('Dias alugados: {} dias. Valor: R${:.2f}'.format(D,T))
print('O valor total à ser pago é de: R${:.2f}'.format(Q + T))