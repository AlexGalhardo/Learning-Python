valoress = []
valoress.append(5)
valoress.append(9)
valoress.append(4)

for cont in range(0, 4): # peça 4 números aos usuários
	valoress.append(int(input('\t Digite um valor: ')))

for c, v in enumerate(valoress):
	print('\t Na posicao {} encontrei o valor {}'.format(c, v))


print('\n\t Cheguei ao final da Lista')
