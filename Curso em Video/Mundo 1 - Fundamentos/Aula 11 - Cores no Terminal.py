# ANSI
# ESCAPE SEQUENCE

# \033[m

# \033[style ~ text ~ back m
# \033[style=0:text=33:back=44m

# \033[0:33:44m

# STYLE
# 0 -> none
# 1 -> bold
# 4 -> underline
# 7 -> negative

# TEXT = text color
# back = background Color

print('\033[31mOla Mundo')

print('\033[31;43mOlá, Mundo')

print('\033[4;30;45mOlá Mundo\033[m')

print('\033[37mOla Mundo')

a = 3
a = 5
print('Os valores são \033[32m{}\033 e \033[31m{}'.format(a, b))

nome = 'alex'
print('Olá! Muito prazer em te conhecer , {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))

# dicionario
cores = {'limpa':'\033[m', 
		'azul':'\033[34m', 
		'amarelo': '\033[33m', 
		'pretoebranco':'\033[7;30m'}

print('Ola, muito prazer em te conhecer, {}{}{}'.format(cores['pretoebranco'], nome, cores['limpa']))

