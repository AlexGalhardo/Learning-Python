'''
SEMELHANTES A LISTAS E TUPLAS, MAS PODE TER INDICES COM NOMES
'''

# listas
dados = list()
dados.append('pedro')
dados.append(25)
print(dados[0]) # pedro
print(dados[1]) # 25

# dicionarios 
dicionario = {'nome':'Pedro', 'idade':25}
print(dicionario['nome']) # pedro
print(dicionario['idade']) # 25
dicionario['sexo'] = 'masculino' # vai adicionar no indice 2
del dicionario['idade'] # vai eliminar o indice e seu elemento

filme = {
	'titulo': 'Star Wars',
	'ano': 1997,
	'diretor': 'George Lucas'
}

print(filme.values()) # vai retornar os valores, ou seja, star wars, 1997, george lucas
print(filme.keys()) # vai printar as chaves, ou seja, titulo, ano, diretor
print(filme.items()) # vai printar as chaves com seus valores

for k, v in filme.items():
	print('A chave {}  tem o valor de: {}'.format(k, v)) # a chave titulo tem o valor de : star wars


pessoas = {
	'nome':'alex',
	'sexo': 'm', 
	'idade':20
}
print(pessoas['nome']) # alex
print(pessoas['sexo']) # m
print(pessoas['idade']) # 20
print(pessoas.values()) # ['alex', 'm', 20]
print(pessoas.keys()) # ['nome', 'sexo', 'idade']
print(pessoas.items()) # ([('nome', 'alex'), ('sexo', 'm'), ('idade', 20)])

del pessoas['sexo'] # deleta a chave e o valor
pessoas['nome'] = 'xande' # muda o valor da chave nome para xande

print(brasil)

estado = dict()
brasil = list()

for c in range(0, 3):
	estado['uf'] = str(input('Unidade Federativa: '))
	estado['sigla'] = str(input('Sigla do Estado: '))
	brasil.append(estado.copy())

print(brasil)
for e in brasil:
	for k, v in e.items():
		print('O campo {} tem valor {}'.format(k, v))