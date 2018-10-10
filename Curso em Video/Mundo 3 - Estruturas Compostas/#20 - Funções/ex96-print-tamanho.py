def printTamanho(string):
	tamanhoString = len(string) 
	print('-' * tamanhoString)
	print('{}'.format(string))
	print('-' * tamanhoString)

printTamanho('Ola Mundo')
printTamanho('Meu nome é alex galhardo')