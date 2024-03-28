# testando o módulo math

# import math                      importa todas as funcionalidades de math
# from math import X               importa apenas a propriedade que vc selecionar

from math import sqrt

N1 = int(input('Digite um número: '))
R = sqrt(N1)

print('A quaiz quadra de {} é {:.0f}'.format(N1,R))