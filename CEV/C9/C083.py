"""""
Exercício Python 083: 
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""""

E = str(input("Digite uma expressão matemática: "))

L = [char for char in E]

X = L.count("(")
Y = L.count(")")

if X == Y:
    print('\033[1;32mSua expressão é válida!\033[m')

else:
    print('\033[1;31mExpressão inválida!\033[m Tente novamente.')


