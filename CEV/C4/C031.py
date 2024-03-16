# Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
# .

K = float(input('Digite a distânica (KM) da sua viagem: '))

if K <= 200:

    V = K * 0.5

    print('Distância da sua viagem: {}Km'.format(K))
    print('O custo da sua viagem é de: R${:.2f}'.format(V))

else:

    V = K * 0.45

    print('Distância da sua viagem: {}Km'.format(K))
    print('O custo da sua viagem é de: R${:.2f}'.format(V))