'''
def fatorial(n):
	f = 1
	for c in range(1, n+1):
		f *= c
	return f

def dobro(n):
	return n * 2

def triple(n):
	return n * 3
'''

# importando o módulo uteis
import uteis

# versão específica que apenas chama a função do módulo específico
# não é recomendado, porque pode causar incompatibilidades
# from uteis import fatorial, dobro

# mesma coisa é com modulos nativos
# from math import sqrt
# from random import randint

# módulos são excelentes para organização dó código
# facilidade de manutenção
# ocultação de códigos detalhados
# reutilização de outros projetos

# no python, chamamos PACOTE uma pasta que contem módulos
# em python, TODA PASTA É CONSIDERADA UM PACOTE
# PASTA/PACOTE uteis 
'''
  - cores
  - datas
  - números
  - strings
  - etc
'''
# IMPORTANDO UM PACOTE
from pacote_uteis import numeros

num = int(input("Digite um valor: "))
# usando a função fatorial() do módulo uteis.py
fat = uteis.fatorial(num)
print("O fatorial de {} é {}!".format(num, fat))