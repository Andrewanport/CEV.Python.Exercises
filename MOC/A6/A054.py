# Criando uma ligação de uma lista:

test = list()

test.append('Gustavo')
test.append(40)

galera = list()
galera.append(test)

test[0] = 'Maria'
test[1] = 22

galera.append(test)
print(galera)

# tudo foi modificado porque as listas estão interligadas
