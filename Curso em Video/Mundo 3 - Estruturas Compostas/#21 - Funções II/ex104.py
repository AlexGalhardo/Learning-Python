def leiaInt(frase):
	numero = input(f'{frase}')
	while type(numero) is not int or type(numero) is str:
		print('ERRO! Digite um número inteiro válido.')
		numero = int(input(f'{frase}'))
	return numero

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')