lista = []

for valor in range(0, 10):
	valorParaAdicionar = int(input('\t Digite um valor: '))
	for index, numero in enumerate(lista):
		if valorParaAdicionar < numero:
			lista.insert(index, valorParaAdicionar)
			print('\t {} adicionado na posicao {}'.format(valorParaAdicionar, index))

	for index, valor in enumerate(lista):
		print(index)
		if lista[index] < valorParaAdicionar:
			continue
		elif lista[index] > valorParaAdicionar:
			lista.insert(index, valorParaAdicionar)
			print('\t Valor {} adicionado na posicao {}.'.format(valorParaAdicionar, index))
		'''
		if valorParaAdicionar < menor:
			lista.insert(index, valorParaAdicionar)
		elif valorParaAdicionar > maior:
			lista.insert(index, valorParaAdicionar)
		'''

print('\t Printando a lista final...\n')
for index, valor in enumerate(lista):
	print('\t Valor na posicao {}: {}'.format(index, valor))