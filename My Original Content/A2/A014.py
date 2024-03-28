N1 = int(input('Digite a sua nota (1): '))
N2 = int(input('Digite a sua nota (2): '))

M = (N1 + N2) / 2

print('A sua média é {:.1f}'.format(M))

if M >= 6:
    print('Você passou de ano!')

else:
    print('Você vai para recuperação!')