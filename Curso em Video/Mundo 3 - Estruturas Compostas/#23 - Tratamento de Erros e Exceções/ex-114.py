import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    # print(f'\033[0;31mO site Pudim não está acessível no momento.\033[m')
    print(f'Site do pudim não disponível no momento!')
else:
    # print(f'\033[0;34mConsegui acessar o site Pudim com sucesso!\033[m')
	print('Site do pudim acessível no momento!')