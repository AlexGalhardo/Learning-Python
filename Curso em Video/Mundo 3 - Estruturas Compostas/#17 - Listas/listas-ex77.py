lista = []
# peça 5 numeros ao usuário
for index, num in enumerate(range(0, 5)):
	lista.append(int(input('\t Digite um valor para a posicao {}: '.format(index))))

maior = lista[0]
menor = lista[0]

for numero in lista:
	if numero > maior:
		maior = numero
	elif numero < menor:
		menor = numero

print('\n\n\t O maior numero é: {}'.format(maior))
print('\t O menor numero é: {}'.format(menor))