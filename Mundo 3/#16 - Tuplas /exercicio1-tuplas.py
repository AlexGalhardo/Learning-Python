numeros1 = ('um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
numeros2 = ('onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
numeros = numeros1+numeros2

numeroUsuario = int(input('\t Digite um numero entre 0 e 20: '))
if numeroUsuario > len(numeros):
	print('Voce digitou um numero invalido. Tente novamente')
elif numeroUsuario < 0:
	print('Voce digitou um numero invalido. Tente novamente')
else:
	print('\t Voce digitou o numero {}'.format(numeros[numeroUsuario-1]))