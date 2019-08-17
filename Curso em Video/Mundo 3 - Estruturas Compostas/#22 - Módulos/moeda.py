def aumentar(n=0, porc, bol):
	if bol:
		return "R$ {}".format(float(n * ((100+porc)/100)))
	else:
		return float(n * ((100+porc)/100))

def diminuir(n=0, porc2, bol):
	if bol:
		return "R$ {}".format(float(n * ((100 - porc2)/100)))
	else:
		return float(n * ((100 - porc2)/100))

def dobro(n=0, bol):
	if bol:
		return "R$ {}".format(n * 2)
	else:
		return n * 2

def metade(n=0, bol):
	if bol:
		return "R$ {}".format((n/2))
	else:
		return (n / 2)

# função moeda do módulo moeda.py
# def moeda(preco = 0, moeda = 'R$'):
#	return '{moeda}{preco}'.format(moeda, preco:>8.2f).replace('.', '')

def resumo(n, aumentado, diminuido):
	print('-'*35)
	print('     RESUMO DO VALOR     ')
	print('-'*35)
	print('Preco analisado: \t R$ {}'.format(n))
	print('Dobro do preço: \t R$ {}'.format(dobro(n, False)))
	print('Metade do preço: \t R$ {}'.format(metade(n, False)))
	print('{} de aumento: \t R$ {}'.format(aumentado, aumentar(n, aumentado, False)))
	print('{} de redução: \t R$ {}'.format(diminuido, diminuir(n, diminuido, False)))
	print('-'*35)