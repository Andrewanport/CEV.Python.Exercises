"""""
Exercício Python 081: 
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""""

List = []

R = 'S'

while R == 'S':
    N = int(input('Digite um valor inteiro: '))

    if N in List:
        print('\033[1;31mValor duplicado!\033[m Não foi possível adicionar à lista')
        R = str(input('Deseja continuar? [S/N]')).upper()

    else:
        List.append(N)
        print('\033[1;32mValor adcionado com sucesso!\033[m')
        R = str(input('Deseja continuar? [S/N]')).upper()

print(f'A ordem crescente da lista é: {sorted(List)}')
print(f'Quantidade de números digitados: {len(List)}')
print(f'Ordem decrescente da lista: {sorted(List, reverse=True)}')

if 5 in List:
    print(f'O valor 5 \033[1;32mESTÁ\033[m na lista')
else:
    print(f'O valor 5 \033[1;31mNÃO\033[m foi adicionado à lista')