dados = dict()
for c in range(0, 1):
	dados['nome'] = str(input('Nome: '))
	dados['nascimento'] = int(input('Ano de Nascimento: '))
	dados['idade'] = 2018 - dados['nascimento']
	if dados['idade'] < 18:
		print('\n\n')
		print(dados.items())
		for k, v in dados.items():
			print('\t {} tem o valor de {}'.format(k, v))
		break
	dados['CLT'] = int(input('Carteira de Trabalho (0 não tem): '))
	if dados['CLT'] == 0:
		print('\n\n')
		del dados['CLT']
		print(dados.items())
		for k, v in dados.items():
			print('\t {} tem o valor de {}'.format(k, v))
		break
	dados['contratacao'] = int(input('Ano de contratacao: '))
	dados['salario'] = int(input('Salário: R$ '))
	print('\n\n')
	print(dados.items())
	for k, v in dados.items():
		print('\t {} tem o valor de {}'.format(k, v))

