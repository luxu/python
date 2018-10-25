import requests
import configparser

# Carrega as configurações de arquivo externo
config = configparser.ConfigParser()
config.read('config.ini')

params = {'login':config['luciano']['loginGmail'],'senha':config['luciano']['senhaGmail']}

def cookie(self):
	r = requests.post(self, params)
	print("Cookie is set to:")
	print(r.cookies.get_dict())
	print('-'*30)
	print("Going to profile page...")
	logar = 'http://controle.luxu.com.br/index.php'
	r = requests.post(logar, cookies=r.cookies)
	print(r.text)

def sessao(self, params):
	session = requests.Session()
	s = session.post(self, params)
	print("Cookie is set to:")
	print(s.cookies.get_dict())
	print('-'*60)
	print("Going to profile page...")
	logar = 'http://controle.luxu.com.br/index.php'
	s = session.get(logar)
	# print(s.text)

site = 'http://controle.luxu.com.br/includes/login.php'
# site = 'http://www.luxu.com.br/Controle/'
# site =  'http://controle.luxu.com.br/includes/autentica.php'
# cookie(site)
sessao(site, params)