def leiaNumbers():
	
	# numInt = int(input('Digite um número inteiro: '))
	# while type(numInt) != int:
	while True:
		try:
			numInt = int(input('Digite um número inteiro: '))
			break
		except:
			print(f'ERRO: por favor, digite um número inteiro válido.')

	# numFloat = float(input('Digite um número real: '))
	# while type(numFloat) != float:
	while True:
		try:
			numFloat = float(input('Digite um número real: '))
			break
		except:
			print(f'ERRO: por favor, digite um número real')

	print(f'O valor inteiro foi: {numInt} e o valor real foi: {numFloat:.2f}')

leiaNumbers()