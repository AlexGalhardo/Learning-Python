from time import sleep

def despacotamento(*numeros):
	print('-='*20)
	maior = -99999
	for parametro in numeros:
		print('{} '.format(parametro), end='')
		sleep(0.5)
		if(parametro > maior):
			maior = parametro
	print('\nO numero total de numeros informados foram: {}.'.format(len(numeros)))
	print('O maior numero informado foi: {}.'.format(maior))
	print('-='*20)

despacotamento(3, 4, 5, 6, )