
# Recebimento de dados do usuário

SB = float(input('Digite o valor do salário bruto: '))

# Cálculo do IR, INSS & SL
IR = 0.10 * SB
INSS = 0.15 * (SB - IR)
SL = SB - IR - INSS

# Saída
print('O valor do IR é {}'.format(IR))
print('O valor do INSS é {}'.format(INSS))
print('O valor do Salário Líquido é {}'.format(SL))