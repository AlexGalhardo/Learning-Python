from random import randint
print('-'*40)
print('\tJOGOS NA MEGA SENA')
print('-'*40)

quantosJogos = int(input('Quantos jogos você quer que eu sorteie: '))
jogos = list()
jogo = list()

for qtdJogo in range(0, quantosJogos):
	for jogada in range(0, 6):
		numero = randint(1, 60)
		jogo.append(numero)
	jogos.append(jogo[:])
	jogo.clear()

for index, jogadaFeita in enumerate(jogos):
	print('Jogada numero {}: {}'.format(index, jogadaFeita))


