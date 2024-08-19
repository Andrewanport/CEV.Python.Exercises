
from random import randint

A1 = randint(0, 100)
A2 = randint(0, 100)
A3 = randint(0, 100)
A4 = randint(0, 100)
A5 = randint(0, 100)

Lista = [A1, A2, A3, A4, A5]

print(f'Os números sorteados foram: {Lista}')

Lista.sort()
print(f'A ordem CRESCENTE dos números é: {Lista}')

Lista.sort(reverse=True)
print(f'A ordem DECRESCENTE dos números é: {Lista}')