def notas(*nums, situacao=False):
	dicionario = dict()
	totalNotas = 0
	valorNotas = 0
	maior = 0
	menor = 10
	media = 0
	for parametro in nums:
		if type(parametro) is bool:
			break 
		valorNotas += parametro
		totalNotas += 1
		if parametro > maior:
			maior = parametro
		if parametro < menor:
			menor = parametro
	dicionario['total'] = totalNotas;
	dicionario['maior'] = maior;
	dicionario['menor'] = menor;
	media = valorNotas / totalNotas
	dicionario['media'] = media
	if situacao:
		if media > 5:
			dicionario['situacao'] = 'BOA'
		else:
			dicionario['situacao'] = 'RUIM'
	return dicionario

resp = notas(3, 6, 10, 10, True)
print(resp)