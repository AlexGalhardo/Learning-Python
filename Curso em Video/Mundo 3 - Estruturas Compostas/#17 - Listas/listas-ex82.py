listaGeral = []
listaImpar = []
listaPar = []

for numero in range(0, 10):
	valorParaAdicionar = int(input('\t Digite um valor: '))
	if (valorParaAdicionar % 2) == 0:
		listaPar.append(valorParaAdicionar)
	else:
		listaImpar.append(valorParaAdicionar)
	listaGeral.append(valorParaAdicionar)

print('\t ...Mostrando lista geral...')
for valor in listaGeral:
	print('\t Numero: {}'.format(valor))

print('\t ...Mostrando lista impar...')
for valor in listaImpar:
	print('\t Numero impar: {}'.format(valor))

print('\t ...Mostrando lista par...')
for valor in listaPar:
	print('\t Numero par: {}'.format(valor))