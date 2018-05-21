produtos1 = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00)
produtos2 = ('Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
produtos = produtos1+produtos2

listaProdutos = []
listaIndices = []

print('-------------------------------------')
print('	LISTAGEM DE PREÇOS          ')
print('-------------------------------------\n')

for index, item in enumerate(produtos):
	index += 1
	if index % 2 == 0:
		listaIndices.append(item)
	else:
		listaProdutos.append(item)

tamanho = len(produtos) / 2
i = 0
while tamanho:
	print('\t {}.....R$   {}'.format(listaProdutos[i], listaIndices[i]))
	i += 1
	tamanho -= 1


