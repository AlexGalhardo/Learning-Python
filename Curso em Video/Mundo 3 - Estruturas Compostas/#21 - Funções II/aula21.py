# ajuda interativa
help()
# para sair
help> quit

# ou de outro modo
help(print)

# direto no print
print(input.__doc__)

# doc strings
def contador(i, f, p):
	'''
	fazendo doc strings aqui da função
	-> faaz uma contagem e mostra na tela
	:param i: inicio da contagem
	:param f: fim da contagem
	:return: sem retorno	
	Função criada por Alex Galhardo
	'''
	c = i
	while c <= f:
		print('{} '.format(c), end='')
	print('fim!')

contador(2, 10, 2)
help(contador)


## Parâmetros opcionais
def somar(a=0, b=0, c=0):
	'''
	Doc strings da função aqui dentro
	'''
	s = a+b+c
	print('A soma é: {}'.format(s))


somar(3, 2, 5)
somar(8,4) # como c não foi informado, 
# o parâmetro opcional c fica com 0
# se eu não informar os parametros opcionais
# vai dar erro na função

def teste(item):
	# quando eu uso a palavra 'global'
	# eu definoa a variável a para usar o seu
	# valor global, ou seja 5, e não 8
	global a
	# se eu não usar 'global a'
	# é como se eu criasse uma nova variável
	# dentro deste escopo da função
	# chamada a que possui o valor 8
	a = 8
	b += 4
	c = 2
	print(f'A dentro vale {a}')
	print(f'B dentro vale {b}')
	print(f'C dentro vale {c}')

a = 5
teste(a)
print(f'A fora vale {a}')


# retorno de valores
def somar(a=0, b=0, c=0):
	s = a+b+c
	return s
	# print(f'A soma vale {s}')

somar(1, 2, 3)
somaeh = somar(3, 4)
print(f'A soma é {somaeh}')