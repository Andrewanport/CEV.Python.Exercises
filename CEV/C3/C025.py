# Crie um programa que leia um nome e diga se tem 'Silva'
# .

nome = str(input('Qual o seu nome? ')).strip()
print('Seu nome possui "SILVA"? {}'.format('SILVA' in nome.upper().split()))