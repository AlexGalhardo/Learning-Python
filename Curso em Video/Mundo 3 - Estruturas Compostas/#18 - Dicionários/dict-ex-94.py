totalPessoas = 0
totalIdade = 0
mediaIdade = 0

dados = dict()
listaMasculino = list()
listaFeminino = list()
dadosPessoa = dict()
dados['M'] = dict()
dados['F'] = dict()

while True:
	dadosPessoa['nome'] = str(input('Nome: '))
	dadosPessoa['sexo'] = str(input('Sexo: [M/F]: ')).upper()
	dadosPessoa['idade'] = int(input('Idade: '))
	totalPessoas += 1
	totalIdade += dadosPessoa['idade']
	if dadosPessoa['sexo'].upper() == 'M':
		listaMasculino.append(dadosPessoa.copy())
	else:
		listaFeminino.append(dadosPessoa.copy())
	continuar = str(input('Quer continuar? [S/N]:' )).upper()
	if continuar.upper() == 'N':
		break

dados['M'] = listaMasculino.copy()
dados['F'] = listaFeminino.copy()
mediaIdade = totalIdade / totalPessoas

print('-='*25)
print('- O grupo tem {} pessoas'.format(totalPessoas))
print('- A média de idade é de {} anos'.format(mediaIdade))
print('As mulheres cadastradas foram: '.format(end=''))
for mulher in dados['F']:
	print('{} '.format(mulher['nome'], end=''))
print('Os homens cadastrados foram: '.format(end=''))
for homem in dados['M']:
	print('{} '.format(homem['nome'], end=''))

print('- Lista das pessoas que estão acima da média: ')
acimaMediaHomem = 0
nomeHomem = 'nada'
for key, valorM in enumerate(dados['M']):
	if valorM['idade'] > acimaMediaHomem:
		acimaMediaHomem = valorM['idade']
		nomeHomem = valorM['nome']
print('nome = {}; sexo = M; idade = {};'.format(nomeHomem, acimaMediaHomem))

print('\n\n')

acimaMediaMulher = 0
nomeMulher = 'nada'
for key, valorF in enumerate(dados['F']):
	if valorF['idade'] > acimaMediaMulher:
		acimaMediaMulher = valorF['idade']
		nomeMulher = valorF['nome']
print('nome = {}; sexo = F; idade = {};'.format(nomeMulher, acimaMediaMulher))
