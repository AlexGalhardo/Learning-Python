lista = []

# peça 10 numeros para o usuário
# não adicione na lista os numeros duplicados
for index, numero in enumerate(range(0, 10)):
	valorParaAdicionar = int(input('\t Digite um valor para a posicao {}: '.format(index)))
	if valorParaAdicionar in lista:
		print('\n\t Valor {} já adicionado na lista.\n\t Esse número não foi adicionado!\n'.format(valorParaAdicionar))
		continue
	else:
		lista.append(valorParaAdicionar)

lista.sort() # ordene a lista em ordem crescente
print('\n\t Printando a lista em ordem crescente...')
for index, numero in enumerate(lista):
	print('\t Valor no index {}: {}'.format(index, numero))