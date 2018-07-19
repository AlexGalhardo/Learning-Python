pessoas = list()
dados = list()

maisPesados = list()
maisLeves = list()

totalPessoas = 0
while True:
	dados.append(str(input('Nome: ')))
	dados.append(int(input('Peso: ')))
	if dados[1] > 100:
		maisPesados.append(dados[:])
	if dados[1] <= 70:
		maisLeves.append(dados[:])
	pessoas.append(dados[:])
	dados.clear()
	totalPessoas += 1
	continuar = str(input('Quer continuar: [S/N]')).upper()
	if continuar == 'N':
		break

print('Ao todo você cadastrou {} pessoas.'.format(totalPessoas))
for dadosPesados in maisPesados:
	print(dadosPesados)
	print('O maior peso foi de {} Kg. Pesos de {}'.format(dadosPesados[1], dadosPesados[0]))

for dadosLeves in maisLeves:
	print(dadosLeves)
	print('O maior peso foi de {} Kg. Pesos de {}'.format(dadosLeves[1], dadosLeves[0]))