lista = []

for numero in range(0, 10):
	lista.append(int(input('\t Digite um numero: ')))

print('\t Total de numeros digitados: {}'.format(len(lista)))

print('\n\t ...Printando valores em ordem decrescente...')
lista.sort(reverse=True)
for index, valor in enumerate(lista):
	print('\t Valor na posicao {}: {}'.format(index, valor))

for numero in lista:
	if numero == 5:
		print('\n\t O 5 foi digitado e está na lista!')