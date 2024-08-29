# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"
# .

C = input('Digite o nome da cidade: ').strip()
print(C[:5].upper() == 'SANTO')
