"""""
Exercício Python 076: 
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""""

print(15*'<>')
print(9*' ', end='')
print("WAN'S STORE")
print(15*'<>')

PP = ('Capinha', 199.90,
      'Ipad 12', 6570.60,
      'Mac book', 15275.50,
      'Iphone 20', 12489.90,
      'Apple pen', 449.99,
      'Cabo', 249.95)

for pos in range (0, len(PP)):
    if pos % 2 == 0:
        print(f'{PP[pos]:_<30}', end='')
    else:
        print(f'R${PP[pos]:>7.2f}')

print(15*'<>')
