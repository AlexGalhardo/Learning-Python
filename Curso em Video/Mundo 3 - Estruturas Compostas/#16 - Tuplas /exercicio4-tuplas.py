lista = []
for i in range(0, 4):
	number = int(input('\t Digite o numero: '))
	lista.append(number)

tupla = tuple(lista)
print('\t O numero 9 apareceu {} vezes na tupla.'.format(tupla.count(9)))
print('\t O primeiro 3 foi digitado na posicao {}.'.format(tupla.index(3, 0)))
print('\n\n\t Mostrando os numeros pares da tupla')
for number in tupla:
	if (number % 2) == 0:
		print('\t {}'.format(number))	