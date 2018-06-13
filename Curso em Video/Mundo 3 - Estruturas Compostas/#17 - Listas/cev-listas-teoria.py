# LISTAS SÃO MUTÁVEIS, ou seja, podem mudar os valores
# diferente de tuplas que são IMUTÁVEIS / nao é permitido mudar os valores

lancheTupla = () # tuplas
lancheLista = [] # listas

lancheLista.append('bolo') # adiciona no final da lista
lancheLista.insert(0, 'suco') # adiciona suco no index 0 da lista

del lancheLista[1] # apaga item do index 1 da lista
lancheLista.pop(3) # apaga item do index 3
lancheLista.remove('suco') # apaga o 'PRIMEIRO' item com string 'suco'
lancheLista.pop() # remove o último elemento da lista
lancheLista.remove('pizza') # se não estiver na lista, vai dar um erro

# se pizza estiver dentro da lista lancheLista
if 'pizza' in lanche:
	lancheLista.remove('pizza')


valores = list(range(4, 11))
# vai criar uma lista chamada valores, com os numeros de 4 a 11
valores = [4, 5, 6, 7, 8, 9, 10] # lembrando que 11 não entra

# ORDENAR LISTA ==> usar .sort()
listaDesordenada = [8, 7, 6, 1, 3, 22, 59, 3]
listaDesordenada.sort() # ordena a lista, do menor para o maior
listaDesordenada.sort(reverse=True) # ordena a lista na ordem reversa, do maior para o menor

len(listaDesordenada) # diz quantos elementos possui dentro da lista

