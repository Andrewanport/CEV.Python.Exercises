
from random import randint

V = randint(10,220)

if V <= 80:
    print('Seu carro estava à {}Km/h.'.format(V))
    print('Você estava dentro do limite de velocidade.')

else:
    print('Multado! Seu carro estava à {}km/h.'.format(V))
    print('Você ultrapassou o limite de velocidade em {}Km/h.'.format(V - 80))

    M = (V-80) * 5.35

    print('Valor à ser pago: R${:.2f}'.format(M))
