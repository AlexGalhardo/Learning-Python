matriz = list()
linhaMatriz = list()

somaPares = 0
somaTerceiraColuna = 0
maiorValorSegundaLinha = 0

for numero in range(0, 3):
	for linha in range(0, 3):
		linhaMatriz.append(int(input('Numero: ')))
	for numero in linhaMatriz:
		if numero % 2 == 0:
			somaPares += numero
	somaTerceiraColuna += linhaMatriz[2]
	matriz.append(linhaMatriz[:])
	linhaMatriz.clear()

#print(matriz)

print('\n\t A Matriz é: \n\n')
for linha in matriz:
	print('[{} | {} | {}]'.format(linha[0], linha[1], linha[2]))

for numero in matriz[1]:
	if numero > maiorValorSegundaLinha:
		maiorValorSegundaLinha = numero

print('\n\t A soma dos valores pares é: {}'.format(somaPares))
print('\n\t A soma dos valores na terceira coluna é: {}'.format(somaTerceiraColuna))
print('\n\t O maior valor da segunda linha é: {}'.format(maiorValorSegundaLinha))