lista = []
for c in range(0, 5):
	n = int(input('Digite um valor: '))
	if c == 0 or n > lista[-1]:
		lista.append(n)
		print('Adicionado ao final da lista...')
	else:
		pos = 0
		# 1, 2, 4, , 6 
		while pos < len(lista):
			# se o numero for menor ou igual a 6, 5 é menor do que 6
			if n <= lista[pos]:
				lista.insert(pos, n)
				print('Adicionado na posicao {} da lista'.format(pos))
				break
			pos += 1

print('-=' * 30)
print('Os valores digitados em ordem foram {}'.format(lista))

