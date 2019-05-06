# import moeda

p = float(input('Digite o preço: R$ '))

# EXERCICIO 107, 108, 109
# print('A metade de R$ {} é {}'.format(p, moeda.metade(p, True)))
# print('O dobro de R$ {} é {}'.format(p, moeda.dobro(p, True)))
# print('Aumentando 10% de {}, temos {}'.format(p, moeda.aumentar(p, 10, True)))
# print('Reduzindo 15% de {}, temos {}'.format(p, moeda.diminuir(p, 15, True)))

# EXERCICIO 110
# moeda.resumo(p, 80, 35)

# EXERCICIO 111 
# from utilidadesCEV import moedas
# moedas.resumo(p, 80, 35)

# EXERCICIO 112
from utilidadesCEV import moedas, dados
p = dados.leiaDinheiro('Digite o preço: R$ ')
moedas.resumo(p, 80, 35)