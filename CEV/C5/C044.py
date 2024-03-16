# Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

print(('=' * 10) + ' Loja do Wan ' + ('=' * 10))

P = float(input('Valor à pagar: R$'))

print('Selecione o método de pagamento:'
      '\n [1] Pix'
      '\n [2] Cartão (1x)'
      '\n [3] Cartão (2X)'
      '\n [4] Cartão (3X à 12X)')

M = int(input('Método de pagamento: '))

if M == 1:
    V = P - (P * 0.1)
    print('Valor à pagar: R${}'.format(V))
    quit()

elif M == 2:
    V = P - (P * 0.05)
    print('Valor à pagar: R${}'.format(V))
    quit()

elif M == 3:
    V = P
    print('Valor à pagar: R${}'.format(V))
    quit()

elif M == 4:
    V = P + (P * 0.20)
    print('Valor à pagar: R${}'.format(V))
    quit()

else:
    print('\033[1;31mOpção INVÁLIDA. Tente novamente.')