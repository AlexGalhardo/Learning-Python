# TUPLAS -> () -> SÃO IMUTAVÉIS
# LISTAS -> [] -> SÃO MUTAVEIS
# DICIONAIS -> {} -> CHAVE: VALOR
lanche = ('hamburguer', 'suco', 'pudim')
#for comida in lanche:
#	print(f'Eu vou comer {comida}')
print('Comi pra caramba')

for cont in range(0, len(lanche)):
	print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
	print(f'Eu vou comer {comida} na posição {pos}')

a = (2, 3, 4)
b = (5, 6, 7)
c = a+b
print(c)
print(c.index(4))
print(c.count(3))

d = (5, 1, 2, 3, 4, 5, 6, 7)
print(d.index(5, 1)) # deslocamento -> que posição está o 5, começando do indice 1
pessoa = ('alex', 'brasileiro')
del(pessoa) # posso deletar uma tupla inteira
del(pessoa[1]) # NÃO posso deletar um indice de uma tupla, pq ela é imutável

numeros1 = ('um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
numeros2 = ('onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
numeros = numeros1+numeros2

numeroUsuario = int(input('\t Digite um numero entre 0 e 20: '))
if numeroUsuario > len(numeros):
	print('Voce digitou um numero invalido. Tente novamente')
elif numeroUsuario < 0:
	print('Voce digitou um numero invalido. Tente novamente')
else:
	print('Voce digitou o numero {}'.format(numeros[numeroUsuario-1]))



