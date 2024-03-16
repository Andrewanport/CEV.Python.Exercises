# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

F = input('Digite uma frase: ').upper().strip()

print('A letra A aparece: {} vezes'.format(F.count('A')))
print('A letra A aparece primeiro na posição: {}'.format(F.find('A') + 1))
print('A letra A aparece por último na posição: {}'.format(F.rfind('A') + 1))

print(F)


