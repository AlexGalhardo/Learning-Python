def fatorial(num=1):
	f = 1
	for c in range(num, 0, -1):
		f *= c
	return f

f1 = fatorial(5)
f2 = fatorial(10)

print(f'Os resultados são {f1} e {f2}')