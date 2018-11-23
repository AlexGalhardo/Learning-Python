def frase(name='desconhecido', gols=0):
	print(f'O jogador {name} fez {gols}(s) gols no compeonato.')

nome = str(input('Nom do Jogador: '))
gols = int(input('Número de Gols: '))

frase(nome, gols)