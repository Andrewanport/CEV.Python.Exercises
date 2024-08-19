"""""
Exercício Python 083: 
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""""

expr = str(input('Digite uma expressão matemática: '))

pilha = []

for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        pilha.append('(')
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')

if len(pilha) == 0:
    print('\033[1;32mSua expressão é válida!\033[m')

else:
    print('\033[1;31mExpressão inválida!\033[m Tente novamente.')