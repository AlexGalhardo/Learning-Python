from random import randint

lista = []

def geraNumeros(lista):
	count = 5
	print('-='*20)
	while count:
		number = randint(1, 50)
		lista.append(number)
		count -= 1
	print('A lista gerada foi: ', end='')
	for number in lista:
		print('{} '.format(number), end='')


def somaPares(lista):
	soma = 0
	print('\nSomando os valores pares: ', end='')
	for number in lista:
		if number % 2 == 0:
			soma += number
			print('{} '.format(number), end='')
	print(' Temos a soma de {}.'.format(soma))
	print('-='*20)


geraNumeros(lista)
somaPares(lista)
geraNumeros(lista)
somaPares(lista)
geraNumeros(lista)
somaPares(lista)
