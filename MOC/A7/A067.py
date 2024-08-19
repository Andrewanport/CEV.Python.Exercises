print('~~' * 25)
print('                \033[1;32mTABELA DA VERDADE\033[m                ')
print('~~' * 25)

L = []
F = str(input('Digite uma frase: '))

print('~~' * 25)
X = int(input(('| [1] == Simples'
               '\n| [2] == Composta [E]'
               '\n| [3] == Composta [OU]'
               '\n| [4] == Composta [OU... OU]'
               '\n| [5] == Composta [SE... ENTÃO]'
               '\n| [6] == Composta [SE E SOMENTE SE]'
               '\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
               '\n| Selecione o tipo de frase que deseja avaliar: ')))

print('~~' * 25)
print(f'Opção selecionada: \033[1;32m[{X}]\033[m ')
print('~~' * 25)

# True or False != 1
if X != 1:

    # Lista
    L = []

    for i in range(2):
        TF = int(input('Selecione o valor lógico da primeira proposição {0}:'
                       '\n[0] Falso'
                       '\n[1] Verdadeiro'
                       '\n-> '.format(i + 1)))
        L.append(TF)
    print('~~' * 25)

# CONDICIONAL [1] == simples
if X == 1:

    # True or False
    TF = int(input('Selecione o valor lógico da frase em questão:'
                   '\n[0] Falso'
                   '\n[1] Verdadeiro'
                   '\n-> '))

    print('~~' * 25)

    # Condicional
    if TF == 0:
        print('A proposição é \033[1;31mFALSA\033[m')

    elif TF == 1:
        print('A proposição é \033[1;32mVERDADEIRA\033[m')

    print('~~' * 25)

    # Negação ou Afirmação
    NB = int(input('Selecione o que deseja:'
                   '\n[0] Valor lógico da \033[1;31mNEGAÇÃO\033[m da frase'
                   '\n[1] Valor lógico da \033[1;32mAFIRMAÇÃO\033[m da frase'
                   '\n-> '))

    print('~~' * 25)

    # Condicional
    if TF == NB:
        print('A proposição é \033[1;32mVERDADEIRA\033[m')

    elif TF != NB:
        print('A proposição é \033[1;31mFALSA\033[m')

# CONDICIONAL [2] == Composta [E]
if X == 2:
    if L[0] and L[1] == 1:
        print('A proposição é \033[1;32mVERDADEIRA\033[m')
        P = 1

    else:
        print('A proposição é \033[1;31mFALSA\033[m')
        P = 0

# CONDICIONAL [3] == Composta [OU]
elif X == 3:

    if L[0] or L[1] == 1:
        print('A proposição é \033[1;32mVERDADEIRA\033[m')
        P = 1

    else:
        print('A proposição é \033[1;31mFALSA\033[m')
        P = 0

# CONDICIONAL [4] == Composta [OU... OU]
elif X == 4:

    if L[0] != L[1]:
        print('A proposição é \033[1;32mVERDADEIRA\033[m')
        P = 1

    else:
        print('A proposição é \033[1;31mFALSA\033[m')
        P = 0

# CONDICIONAL [5] == Composta [SE... ENTÃO]
elif X == 5:

    if L[0] == 1 and L[1] == 0:
        print('A proposição é \033[1;31mFALSA\033[m')
        P = 0

    else:
        print('A proposição é \033[1;32mVERDADEIRA\033[m')
        P = 1

# CONDICIONAL [6] == Composta [SE E SOMENTE SE]
elif X == 6:  #

    if L[0] == L[1]:
        print('A proposição é \033[1;32mVERDADEIRA\033[m')
        P = 1

    else:
        print('A proposição é \033[1;31mFALSA\033[m')
        P = 0

print('~~' * 25)

# TABELA (PROTÓTIPO)
if X != 1:
    print(' 1º|2º   |R|')
    print(f'[{L[0]}][{L[1]}] = [{P}]')

    print('~~' * 25)

    # Negação ou Afirmação
    NB = int(input('Selecione o que deseja:'
                   '\n[0] Valor lógico da \033[1;31mNEGAÇÃO\033[m da frase'
                   '\n[1] Valor lógico da \033[1;32mAFIRMAÇÃO\033[m da frase'
                   '\n-> '))

    print('~~' * 25)

    if P == NB:
        print('A proposição é \033[1;32mVERDADEIRA\033[m')

    elif P != NB:
        print('A proposição é \033[1;31mFALSA\033[m')
