'''
crie um programa onde o usuário digite
uma expressão qualquer que use

'''

# exemplo ((a+b)*c)

input = str(input('\t Digite a expressao: '))

chaveParaFechar = 0
for char in input:
	if char == '(':
		chaveParaFechar += 1

for char in input:
	if char == ')':
		chaveParaFechar -= 1

if chaveParaFechar == 0:
	print('\t A expressão É válida.')
else:
	print('\t A expressão NÃO é válida.') 
