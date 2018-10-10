def contagem(inicio, fim, passo):
	print('-='*20)
	if(passo == 0):
		print('Contagem de {} até {} de {} em {}'.format(inicio, fim, 1, 1))
		if(inicio<fim):
			number = inicio
			while number < fim:
				print('{} '.format(number), end='')
				number += 1
			print('-='*20)
		else:
			num = inicio
			while num >= fim:
				print('{} '.format(num), end='')
				num -= 1
			print('\n')
			print('-='*20)
	else:
		print('Contagem de {} até {} de {} em {}'.format(inicio, fim, passo, passo))
		if(inicio<fim):
			number = inicio
			while number < fim:
				print('{} '.format(number), end='')
				number += passo
			print('-='*20)
		else:
			num = inicio
			while num >= fim:
				print('{} '.format(num), end='')
				num -= passo
			print('\n')
			print('-='*20)

contagem(5, -5, 0)