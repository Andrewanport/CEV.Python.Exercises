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

# | [1] == Simples  ---------------------------------------------------------------------------------------------------
if X == 1:
    print('~~' * 25)
    print('Opção selecionada: \033[1;32m[1] == Simples\033[m ')
    print('~~' * 25)

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
        print('A proposição é \033[1;32mVERDADEIRA\033[1;32m')

    elif TF != NB:
        print('A proposição é \033[1;31mFALSA\033[m')

# | [2] == Composta [E] -----------------------------------------------------------------------------------------------
if X == 2:
    print('~~' * 25)
    print('Opção selecionada: \033[1;32m[2] == Composta [E]\033[m ')
    print('~~' * 25)

    # Lista
    L = []

    # True or False
    for i in range(2):
        TF = int(input('Selecione o valor lógico da primeira proposição {0}:'
                       '\n[0] Falso'
                       '\n[1] Verdadeiro'
                       '\n-> '.format(i + 1)))
        L.append(TF)

    print('~~' * 25)

    # Condicional
    if L[0] and L[1] == 1:
        print('A proposição é \033[1;32mVERDADEIRA\033[m')
        P = 1

    else:
        print('A proposição é \033[1;31mFALSA\033[m')
        P = 0

    print('~~' * 25)

    # TABELA (PROTÓTIPO)
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

# | [3] == Composta [OU] ----------------------------------------------------------------------------------------------
if X == 3:
    print('~~' * 25)
    print('Opção selecionada: \033[1;32m[3] == Composta [OU]\033[m ')
    print('~~' * 25)

    # Lista
    L = []

    # True or False
    for i in range(2):
        TF = int(input('Selecione o valor lógico da primeira proposição {0}:'
                       '\n[0] Falso'
                       '\n[1] Verdadeiro'
                       '\n-> '.format(i + 1)))
        L.append(TF)

    print('~~' * 25)

    # Condicional
    if L[0] or L[1] == 1:
        print('A proposição é \033[1;32mVERDADEIRA\033[m')
        P = 1

    else:
        print('A proposição é \033[1;31mFALSA\033[m')
        P = 0

    print('~~' * 25)

    # TABELA (PROTÓTIPO)
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

# | [4] == Composta [OU... OU] ----------------------------------------------------------------------------------------
if X == 4:
    print('~~' * 25)
    print('Opção selecionada: \033[1;32m[4] == Composta [OU... OU]\033[m ')
    print('~~' * 25)

    # Lista
    L = []

    # True or False
    for i in range(2):
        TF = int(input('Selecione o valor lógico da primeira proposição {0}:'
                       '\n[0] Falso'
                       '\n[1] Verdadeiro'
                       '\n-> '.format(i + 1)))
        L.append(TF)

    print('~~' * 25)

    # Condicional
    if L[0] != L[1]:
        print('A proposição é \033[1;32mVERDADEIRA\033[m')
        P = 1

    else:
        print('A proposição é \033[1;31mFALSA\033[m')
        P = 0

    print('~~' * 25)

    # TABELA (PROTÓTIPO)
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

# | [5] == Composta [SE... ENTÃO] -------------------------------------------------------------------------------------
if X == 5:
    print('~~' * 25)
    print('Opção selecionada: \033[1;32m[5] == Composta [SE... ENTÃO]\033[m ')
    print('~~' * 25)

    # Lista
    L = []

    # True or False
    for i in range(2):
        TF = int(input('Selecione o valor lógico da primeira proposição {0}:'
                       '\n[0] Falso'
                       '\n[1] Verdadeiro'
                       '\n-> '.format(i + 1)))
        L.append(TF)

    print('~~' * 25)

    # Condicional
    if L[0] == 1 and L[1] == 0:
        print('A proposição é \033[1;31mFALSA\033[m')
        P = 0

    else:
        print('A proposição é \033[1;32mVERDADEIRA\033[m')
        P = 1

    print('~~' * 25)

    # TABELA (PROTÓTIPO)
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

# | [6] == Composta [SE E SOMENTE SE] ---------------------------------------------------------------------------------
if X == 6:
    print('~~' * 25)
    print('Opção selecionada: \033[1;32m[6] == Composta [SE E SOMENTE SE]\033[m ')
    print('~~' * 25)

    # Lista
    L = []

    # True or False
    for i in range(2):
        TF = int(input('Selecione o valor lógico da primeira proposição {0}:'
                       '\n[0] Falso'
                       '\n[1] Verdadeiro'
                       '\n-> '.format(i + 1)))
        L.append(TF)

    print('~~' * 25)

    # Condicional
    if L[0] == L[1]:
        print('A proposição é \033[1;32mVERDADEIRA\033[m')
        P = 1

    else:
        print('A proposição é \033[1;31mFALSA\033[m')
        P = 0

    print('~~' * 25)

    # TABELA (PROTÓTIPO)
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

