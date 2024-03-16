# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# .

Nome = input('Digite o seu nome: ').split()

print('Seu primeiro nome é: {}'.format(Nome[0]))
print('Seu útlimo nome é: {}'.format(Nome[len(Nome)-1]))

# Usamos o 'len' porque ele conta quantos índices terão no array que splitamos no começo do código
# Portanto, assim teremos a última unidade contada -1 pois a contagem começa apartir de 0.