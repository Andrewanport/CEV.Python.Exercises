"""""
Exercício Python 072: 
Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até dez. 
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""""

Num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')

while True:

    N = int(input('Digite um número de 0 - 10: '))

    if 0 <= N <= 10:
        break

    else:
        print('Opção inválida, tente novamente')

print(f'Você digitou o número {Num[N]}')