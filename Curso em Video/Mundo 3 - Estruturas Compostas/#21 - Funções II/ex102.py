# fatorial
def fatorial(number, op=False):
	f = 1
	if op == False:
		for c in range(number, 0, -1):
			f *= c
			return f
	else:
		lista = list()
		for c in range(number, 0, -1):
			f *= c
			print(f'{c} x ', end='')
		print(f' = {f}', end='')
		print('\n')
		

print(fatorial(5, False)) # 120
fatorial(5, True)# 5 x 4 x 3 x 2 x 1 = 120