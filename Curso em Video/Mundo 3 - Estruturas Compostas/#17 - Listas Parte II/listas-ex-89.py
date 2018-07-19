'''
boletim = list()
boletimNotas = list()
boletimFinal = list()

while True:
	mediaAluno = 0
	boletimFinal.append(str(input('Nome: ')))
	boletimNotas.append(int(input('Nota 1: ')))
	boletimNotas.append(int(input('Nota 2: ')))
	mediaAluno = (boletimNotas[0] + boletimNotas[1])/2
	boletimFinal.append(mediaAluno)
	boletim.append(boletimFinal[:])
	boletimFinal.clear()
	boletimNotas.clear()
	continuar = str(input('Deseja continuar: [S/N]')).upper()
	if continuar == 'N':
		break

print('-='*20)
print('No.\tNOME\t\tMÉDIA')
print('-'*40)
for index, dados in enumerate(boletim):
	print('{}\t{}\t\t{}'.format(index, dados[0], dados[1]))
print('-'*40)
'''

# EXEMPLO 2
boletim = list()

while True:
	mediaAluno = 0
	indiceAluno = 0
	for nome in range(0, 1):
		boletim[indiceAluno][0].append(str(input('Nome: ')))
		index = 1
		for i in range(0, 2):
			boletim[indiceAluno][1].append(int(input('Nota {}: '.format(index))))
			index+=1
		mediaAluno = (boletim[indiceAluno][1][0]+boletim[indiceAluno][1][1])/2
		boletim[indiceAluno][2].append(mediaAluno)
	indiceAluno+=1
	continuar = str(input('Quer continuar: [S/N]')).upper()
	if continuar == 'N':
		break

print('-='*20)
print('No.\tNOME\t\tMÉDIA')
print('-'*40)
for index, dados in enumerate(boletim):
	print('{}\t{}\t\t{}'.format(index, dados[0], dados[1]))
print('-'*40)