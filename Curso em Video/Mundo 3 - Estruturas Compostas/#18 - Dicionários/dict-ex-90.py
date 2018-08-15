boletim = dict()
dados = []

for dados in range(0, 1):
	boletim['nome'] = str(input('Nome: '))
	boletim['media'] = float(input('Media: '))
	if boletim['media'] < 5:
		boletim['situacao'] = 'reprovado'
	else:
		boletim['situacao'] = 'aprovado'

for k, v in boletim.items():
	print('O {} é {}'.format(k, v))