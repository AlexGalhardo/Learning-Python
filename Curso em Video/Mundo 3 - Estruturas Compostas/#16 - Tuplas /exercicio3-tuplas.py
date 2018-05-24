from random import randint
tupla = ()
lista = list(tupla)
randomNumbers = []

valido = 5
while valido:
	randomNumbers.append(randint(0, 10))
	valido -= 1

maior = 0
menor = 10
for number in randomNumbers:
	lista.append(number)
	if number > maior:
		maior = number
	if number < menor:
		menor = number

print('\t Nova tupla')
print(tuple(lista))
print('\t Maior é --> {}'.format(maior))
print('\t Menor é --> {}'.format(menor))