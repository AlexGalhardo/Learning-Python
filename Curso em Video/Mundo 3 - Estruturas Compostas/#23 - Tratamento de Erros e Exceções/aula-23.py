try:
	# primeiro tente isso
	a = int(input('Numerador: '))
	b = int(input('Denominador: '))
	r = a/b
except:
	# esse tipo de except é o genérico, ou seja
	# pega qualquer tipo de erro
	# se o try não deu certo, caia aqui dentro
	print('Você digitou algo errado')
else:
	# se o try deu certo
	print(f'O resultado é {r} \n')
	print(f'O resultado é {r:.1f}')
finally:
	# vai acontecer independente se deu erro ou não
	print(f'Volte sempre!')


# SEGUNDO EXEMPLO
# é bom pegar o erro aqui neste exemplo
# enquanto estiver desenvolvendo
try:
	# primeiro tente isso
	a = int(input('Numerador: '))
	b = int(input('Denominador: '))
	r = a/b
except Exception as erro:
	# se o try não deu certo, caia aqui dentro
	print(f'O erro encontrado foi {erro.__cause__}')
	print(f'O problema encontrado foi {erro.__class__}')
except ValueError:
	# se deu erro de valor...
	print(f'O problema encontrado foi {erro.__class__}')
except (ValueError, TypeError):
	# conjunto com 2 tipos de erros dentro do mesmo except
	print(f'O problema encontrado foi {erro.__class__}')
except ZeroDivisionError:
	# caso tenha alguma divisão por zero
	print(f'O problema encontrado foi {erro.__class__}')
except KeyboardInterrupt:
	# o usuário preferiu não informar os dados
	print(f'O problema encontrado foi {erro.__class__}')
else:
	# se o try deu certo
	print(f'O resultado é {r} \n')
	print(f'O resultado é {r:.1f}')
finally:
	# vai acontecer independente se deu erro ou não
	print(f'Volte sempre!')