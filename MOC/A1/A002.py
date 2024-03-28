N1 = int(input('Digite um número (1): '))
N2 = int(input('Digite outro número (2): '))
Soma = (N1 + N2)
Mult = (N1 * N2)
Divi = (N1 / N2)

# A forma menos otimizada seria:
# print(' a soma dos números é:', Soma , ', a multiplicação é:', Mult, ' e a divisão é:' , Divi)

# A forma mais inteligente seria:
print('A soma equivale à {}, a multiplicação à {} e a divisão à {:.2f}'.format(Soma, Mult, Divi))

# {:.2f} serve para limitar as casas decimais