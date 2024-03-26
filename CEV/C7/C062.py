"""

Exercício Python 062:
Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.

"""

print('-'*23)
print('PROGRESSÃO ARITMÉTICA ')
print('-'*23)

P = int(input('Digite o início da PA: '))
R = int(input('Digite a razão da PA: '))
D = P + (10 - 1) * R

T = P
C = 1
Total = 0
Mais = 10

while Mais != 0:
    Total += Mais

    while C <= Total:
        print('{} '.format(T), end='⭢ ')
        T += R
        C += 1

    print('PAUSA')
    Mais = int(input('Quantos termos você quer mostrar a mais: '))
print('FIM')

