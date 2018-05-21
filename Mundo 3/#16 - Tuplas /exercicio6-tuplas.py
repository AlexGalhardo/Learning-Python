palavras = ('aprender', 'programar', 'linguagem', 'python',
			'curso', 'gratis', 'estudar', 'praticar',
			'trabalhar', 'mercado', 'programador', 'futuro')

vogais = ['a', 'e', 'i', 'o', 'u']

for palavra in palavras:
	# lista com vogais na palavra
	vogaisNaPalavra = []
	# percorre lista de letras da palavra na tupla
	for letra in palavra:
		if letra in vogais:
			vogaisNaPalavra.append(letra)

	print('\t Na palavra {} temos '.format(palavra), end="")
	for vogal in vogaisNaPalavra:
		print('{} '.format(vogal), end="")
	print('\n')