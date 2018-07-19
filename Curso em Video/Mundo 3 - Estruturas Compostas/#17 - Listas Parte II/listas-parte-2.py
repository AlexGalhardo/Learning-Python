# TEORIA DA AULA 17 -- CURSO PYTHON 
# https://www.youtube.com/watch?v=YV_JQmZNFsk
# lista é mutável
dados = list()
# adiciona pedro no indicie 0
dados.append('pedro')
# adiciona 25 no indice 1
dados.append(25)

print(dados[1]) # printa 25
print(dados[0]) # printa pedro

pessoas = list()
# adiciona uma cópia da lista dados dentro do indice 0 da lista pessoas
pessoas.append(dados[:])
# IMPORTANTE: quando eu uso [:] dentro da lista, eu faço uma cópia
# CASO EU NÃO COLOQUE [:], eu faço uma referência a lista original
# como se fosse o endereço de memória dos dados na lista dados
# [:] ==> CÓPIA
# pessoas.append(dados) ==> REFERÊNCIA ==> ponteiro* e &endereço de memória 

# listas compostas
pessoas2 = [['pedro', 25], ['maria', 19], ['Joao', 32]]
print(pessoas2[0][0]) # vai printar pedro
print(pessoas2[1][1]) # vai printar 19
print(pessoas2[2][0]) # vai printar joao
print(pessoas2[1]) # vai printar ['pedro', 25]


# EXEMPLO 1
galera = [['alex', 20], ['xande', 18], ['maria', 30]]
for lista in galera:
	print(lista)
	print('{} tem {} anos de idade'.format(lista[0], lista[1]))

# EXEMPLO 2
grupo = list()
dados = list()
for c in range(0, 3):
	dados.append(str(input('Nome: ')))
	dados.append(int(input('Idade: ')))
	grupo.append(dados[:])
	# LEMBRANDO QUE [:] É UMA CÓPIA DO DADO
	dados.clear()

print(grupo)
