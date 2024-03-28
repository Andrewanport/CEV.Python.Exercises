# testando o módulo math

# import math                      importa todas as funcionalidades de math
# from math import X               importa apenas a propriedade que vc selecionar

import math

N1 = int(input('Digite um número: '))
R = math.sqrt(N1)

print('A quaiz quadra de {} é {}'.format(N1, math.floor(R)))