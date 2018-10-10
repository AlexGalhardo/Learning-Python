# contador de parâmetros
def contador(* contador):
	for parametro in contador:
		print('{} '.format(parametro), end='')
	print('\nRecebi os valores {} e o total de parametros foi: {}.  '.format(contador, len(contador)), end='')
	print('FIM')

contador(1, 2, 3, 4, 5, 6, 7)