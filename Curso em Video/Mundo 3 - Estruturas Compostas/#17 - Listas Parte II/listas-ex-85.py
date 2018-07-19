listaGeral = list()
pares = list()
impares = list()

# listaGeral = [[], []]

for i in range(0, 7):
	numero = int(input('Numero: '))
	if numero % 2 == 0:
		pares.append(numero)
	else:
		impares.append(numero)

impares.sort()
pares.sort()
listaGeral.append(impares[:])
listaGeral.append(pares[:])
print(listaGeral)