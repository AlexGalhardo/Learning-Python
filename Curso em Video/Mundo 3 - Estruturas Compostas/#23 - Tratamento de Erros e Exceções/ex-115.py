# escrita
# Se tentarmos abrir um arquivo para escrita que não existe, 
# então ele será criado, porém, se ele já existir, 
# todo seu conteúdo será apagado no momento em que abrimos o arquivo.
arquivo = open('dados.txt', 'w')


# Para escrever em um arquivo sem apagar seu contéudo, ou seja, adicionando (incluído) novo conteúdo seguimos 3 passos:
# Ler todo o conteúdo do arquivo,
# efetuar a adição e
# escrever o novo conteúdo no arquivo.

# Abra o arquivo (leitura)
arquivo = open('dados.txt', 'r')
conteudo = arquivo.readlines()

# insira seu conteúdo
# obs: o método append() é proveniente de uma lista
conteudo.append('Nova linha')

# Abre novamente o arquivo (escrita)
# e escreva o conteúdo criado anteriormente nele.
arquivo = open('dados.txt', 'w')
arquivo.writelines(conteudo)
arquivo.close()


# leitura
# Se tentarmos abrir um arquivo para leitura que não existe, um erro será lançado.
arquivo = open('dados.txt', 'r', encoding="utf8")

for line in arquivo:
	print(line)


# Se quisermos ler todo o conteúdo do arquivo em uma única string podemos utilizar a função read().
arquivo = open('dados.txt', 'r')
arquivo.read()


# Podemos utilizar a função readline() caso queiramos ler linha a linha do arquivo.
# A função retornará uma lista vazia [] quando encontrar o final do arquivo (após a última linha ter sido lida).
arquivo = open('dados.txt', 'r')
arquivo.readline()


# Devemos sempre fechar o arquivo aberto.
arquivo.close()
