# Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
# .

N = int(input('Digite um número: '))

# Estética
print('-'*25)

# Tabuada
for c in range(1, 21):

    print('{} x {:2} = {}'.format(N, c, N * c))

# Estética
print('-'*25)