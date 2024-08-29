# Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
# Utilize: F = C x 1,8 + 32.

C = float(input('Digite uma temperatura em celcius: '))

F = C * 1.8 + 32

print('{:.1f}ºC equivalem à {:.1f}ºF'.format(C,F))