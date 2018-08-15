dados = dict()
gols = list()
totalGols = 0

for c in range(0, 1):
	dados['nome'] = str(input('Nome do Jogador: '))
	dados['partidas'] = int(input('Quantas partidas ele jogou: '))
	for partida in range(0, dados['partidas']):
		gols.append(int(input('Quantos gols na partida {}: '.format(partida))))
	for numGols in gols:
		totalGols += numGols
	dados['gols'] = gols
	dados['total'] = totalGols

print('-='*20)
print(dados.items())
print('-='*20)

for k, v in dados.items():
	print('O campo {} tem o valor de {}'.format(k, v))

print('-='*20)
for index, item in enumerate(gols):
	print('\t => Na partida {}, fez {} gols'.format(index, item))

print('Foi um total de {} gols'.format(totalGols))