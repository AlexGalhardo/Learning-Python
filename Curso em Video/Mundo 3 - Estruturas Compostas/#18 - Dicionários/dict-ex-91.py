from random import randint

jogadores = dict()

for c in range(0, 4):
	number = randint(0, 10)
	jogadores[c] = number

for k, v in jogadores.items():
	print('\t O Jogador{} tirou {}'.format(k, v))

print('\n\n')

posicao = 1
for item in sorted(jogadores, key = jogadores.get):
	for k, value in jogadores.items():
		if value == jogadores[item]:
			print('\t Ranking {} Posicao: Jogador{} com {} pontos'.format(posicao, k, value))
			posicao += 1