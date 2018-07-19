matriz = list()
linhaMatriz = list()
for numero in range(0, 3):
	for linha in range(0, 3):
		linhaMatriz.append(int(input('Numero: ')))
	matriz.append(linhaMatriz[:])
	linhaMatriz.clear()

#print(matriz)

print('\n\t A Matriz é: \n\n')
for linha in matriz:
	print('[{} | {} | {}]'.format(linha[0], linha[1], linha[2]))