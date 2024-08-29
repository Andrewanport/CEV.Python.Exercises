"""""
Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou. 
Depois vai ler a quantidade de gols feitos em cada partida. 
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""""

dados = dict()
partidas = list()

print(25 * '~~')
dados['Nome'] = str(input('Nome do jogador: '))

total = int(input(f'Número de partidas de {dados['Nome']}: '))

for x in range(0, total):
    partidas.append(int(input(f'Gols na {x + 1}ª partida: ')))

dados['Gols'] = partidas[:]
dados['Total'] = sum(partidas)

print(25 * '~~')

print(dados)

print(25 * '~~')

for k, v in dados.items():
    print(f'{k} -> {v}')

print(25 * '~~')

print(f'O jogador {dados['Nome']} jogou {len(dados['Gols'])}')

for i, v in enumerate(dados['Gols']):
    print(f'    -> Na partida {i}, fez {v} gols')
print(f'Foi um total de {dados['Total']} gols')
