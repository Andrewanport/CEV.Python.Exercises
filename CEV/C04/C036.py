# Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
# .

V = float(input('Digite o valor do imóvel: '))
S = float(input('Digite o seu salário: '))
A = int(input('Quantos anos pagar: '))

M = V / (A * 12)

if M <= (S * 30) / 100:

    print('Pagamento aprovado para {:.1f} ano(s) !'.format(A))

    print('Valor da prestação: R${:.2f}'.format(M))

else:
    print('Pagamento NÃO aprovado!')
    print('O valor da prestão: R${} excede 30% do salário!'.format(M))

