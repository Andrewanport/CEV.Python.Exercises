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

CP = 0
CV = 1

while len(PP) >= CV:
    print(f'{PP[CP]:_<30} R${PP[CV]}')

    CP += 2
    CV += 2

print(15*'<>')
