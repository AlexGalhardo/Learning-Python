primeiros = ('São Paulo', 'Santos', 'Palmeiras', 'Chapecoense', 'Flamengo', 'Botafogo', 'Corinthians', 'Fluminense', 'Bahia')
segundos = ('Limeira', 'AEA', 'Juventus', 'Barcelona', 'Real Madrid', 'Boca Juniors', 'Sao Caetano', 'Mirassol', 'Gremio', 'Internacional', 'Milan')
tabela = primeiros + segundos

print('\n\t --- Tabela do Brasileirão ---')
for posicao, time in enumerate(tabela):
	print('\t{} esta na {} posicao'.format(time, posicao+1))

print('\n\n\t --- Primeiros 5 colocados ---')
for cont in range(0, 5):
	print('\t {} esta na posicao {}'.format(tabela[cont], cont+1))

print('\n\n\t --- Ultimos 4 colocados ---')
for cont in range(16, 20):
	print('\t {} esta na posicao {}'.format(tabela[cont], cont+1))

print('\n\n\t --- Tabela Ordem Alfabetica ---')
print(sorted(tabela))

print('\n\n\t --- Que posicao está o time da Chapecoense --')
for index, time in enumerate(tabela):
	if time == 'Chapecoense':
		print('\tO time da Chapecoense está na posição: {}\n\n'.format(index));