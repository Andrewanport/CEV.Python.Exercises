# Exercício Python 029: Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.
# .

V = int(input('Digite a velocidade atual do carro: '))

if V <= 80:
    print('Você está dentro do limite de velocidade.')

else:
    print('Multado! Você ultrapassou o limite de velocidade.')

    M = (V-80) * 5.35

    print('Valor à ser pago: R${:.2f}'.format(M))
