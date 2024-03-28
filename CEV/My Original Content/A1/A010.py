frase = 'Curso em Vídeo Python'

print(frase[9])

print(frase[9:21])

print(frase[9:21:2])

print(frase[:5])

print(frase[15:])

print(frase[9::3])

print(len(frase))

print(frase.count('o'))

print(frase.count('o', 0, 13))

print(frase.find('deo'))

print(frase.find('pato')) # -1 significa não encontrado

print('Curso' in frase)

print(frase.replace('Python', 'Java'))

print(frase.upper())

print(frase.lower())

print(frase.lower())

print(frase.capitalize())

print(frase.title())

frase2 = '          Aprenda Python          '

print(frase2.strip()) # tira os espaços desnecessários das extemidades

print(frase2.rstrip()) # remove apenas os do 'right' (direita)

print(frase2.lstrip()) # remove apenas os do 'left' (esquerda)

print(frase.split())

print('-'.join(frase))

print(frase.upper().count('O'))

# Observação sobre a propriedade replace

frase3 = 'Eu gosto de sorvete'
frase3 = frase3.replace('sorvete','chocolate')
print(frase3)

# Agora sim, é possível alterar uma string