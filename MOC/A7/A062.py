
# list = ()
# tupla = []
# dicionário = {}

dados = dict()

dados = {'nome':'Pedro','idade':25,'sexo':'M'}

print(dados['idade'])

dados['comida'] = 'sorvete'

print(dados)

del dados['idade']

print(dados)

filme = {
    'titulo': 'Capitão América',
    'ano': 2004,
    'Diretor': 'Wesley Safadão'
}

print(filme)

print(filme.values())
print(filme.keys())
print(filme.items())

for k, v in filme.items():
    print(f'O {k} é {v}')