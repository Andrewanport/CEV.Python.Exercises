
N = input('Digite seu nome: ')

if N == 'André':
    print('Que nome BONITO, {} !'.format(N))

elif N == 'Pedro' or N == 'Lucas' or N == 'Júlia':
    print('Que nome LEGAL, {} !'.format(N))

elif N in 'Ana Cláudia Jéssica Juliana':
    print('Que nome FEMININO LEGAL, {}'.format(N))

else:
    print('Que nome NORMAL, {} !'.format(N))