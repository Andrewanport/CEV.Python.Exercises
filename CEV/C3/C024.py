# Crie um programa que leia o nome de uma cidade e diga se elae 'S começa ou não com o nomanto'
# .

C = input('Digite o nome da cidade: ').strip()
print(C[:5].upper() == 'SANTO')