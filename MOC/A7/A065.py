
print('<>'*25)
print('                \033[1;32mTABELA DA VERDADE\033[m                ')
print('<>'*25)


F = str(input('Digite uma frase: ')).upper()
NS = int(input('Digite o número de status: '))

"""""
# 1º CASO: quando o número de status (NS) for 1 significa que é uma frase simples, esse será o 1º caso.
"""""

if NS == 1:
    S1 = str(input('Verdadeiro ou falso? [T] [F]: ')).upper()
    Negar = str(input('Deseja a frase base [B], ou a sua respectiva negação? [N]: ')).upper()

    if S1 == 'T' and Negar == 'B':
        print(f'{F} | \033[1;32mVerdadeiro\033[m')

    if S1 == 'F' and Negar == 'B':
        print(f'{F} | \033[1;31mFalsa\033[m')

    if S1 == 'T' and Negar == 'N':
        print(f'{F} | \033[1;31mFalsa\033[m')

    if S1 == 'F' and Negar == 'N':
        print(f'{F} | \033[1;32mVerdadeira\033[m')

"""""
# 2º Caso: quando o número de status (NS) for 2 significa que é uma frase complexa, esse será o 2º caso.
"""""
if NS == 2:

    # [E]
    if ' E ' in F:

        S1 = str(input('[1ª Sentença] Verdadeiro ou falso? [T] [F]: ')).upper()
        S2 = str(input('[2ª Sentença] Verdadeiro ou falso? [T] [F]: ')).upper()

        if S1 and S2 == 'T':
            print(f'{F} | \033[1;32mVerdadeira\033[m')

        else:
            print(f'{F} | \033[1;31mFalsa\033[m')

    # [OU]
        if ' OU ' in F:
            print('ok')
