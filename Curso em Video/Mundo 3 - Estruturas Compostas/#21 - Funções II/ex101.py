def voto(nascimento):
	idade = 2018 - nascimento
	if idade >= 16 and idade < 18:
		"Opcional"
	elif idade > 65:
		return "Opcional"
	else:
		return "OBRIGATÓRIO"

nasc = int(input('Em que ano você nasceu: '))
print(f'Com {nasc} anos o voto é {voto(nasc)}')