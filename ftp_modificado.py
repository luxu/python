from time import sleep
from ftplib import FTP
import os
import json
from pdb import set_trace

file = ""

def conectar(self):
	ftp = FTP(self['ftp'])
	ftp.login(self['login'],self['senha'])
	return ftp

def listar(self,directory):
	self.cwd(directory)
	self.retrlines('LIST')

def download(self,file=None):
	self.retrbinary("RETR {}".format(file), open(file,'wb').write)
	apagar = input(u"{} \n Deletar o arquivo {} (S)im - (N)ão?.: "
		.format('*'*60,file))
	if (apagar == 's' or apagar == 's'.upper()):
		self.delete(file)
		msg = "Arquivo Apagado!"
	msg = "Arquivo não Apagado!"
	self.quit()
	return msg

def limparTela():
	if os.name == 'posix':
		os.system("clear")
	else:
		os.system("cls")

def delete(self):
	self.delete(file)
	self.retrlines('LIST')
	self.quit()

def upload(self,file):
	self.storbinary("STOR {}".format(file), open(file,'rb'))
	# self.quit()

def ftps(options):
	if options == "1":
		fabrizio = {
			"login": "",
			"senha": "",
			"ftp": ""
		}
		connection = conectar(fabrizio)
		listar(connection,'public_html')
		baixar = input("Fazer download?(S)im/(N)ão.: ")
		if (baixar == 's' or baixar == 's'.upper()):
			nome = input("Nome do arquivo.: ")
			print(download(connection,nome))
	elif options == "2":
		luciano = {
			"login": "luxucom",
			"senha": "L3LCoMux@4BrL#",
			"ftp"  : "ftp.luxu.com.br"
		}
		connection = conectar(luciano)
		nome = 'Luciano'
		submenu(connection,nome)
	elif options == "3":
		connection = conectar(fabrizio)
		delete(connection)
		listar(connection,'public_html/telefones')
	elif options == "5":
		print("Saindo...")
		print("")
		sleep(0.3)  # Time in seconds.
		options = "5"
	else:
		print("Esta não é uma opção válida!")
		sleep(0.5)  # Time in seconds.
	return options

def submenu(self, nome):
	limparTela()
	options = ''
	while options != '5':
		print(u"\nQual opção no FTP do {} ?: \n".format(nome))
		print("(1) Downloads\n")
		print("(2) Listar\n")
		print("(3) Upload\n")
		print("(4) Deletar\n")
		print("(5) Sair do FTP\n")
		options = input("Escolha uma das opções acima..:")
		if options == "1":
			baixar = input("Fazer download?(S)im/(N)ão.: ")
			if (baixar == 's' or baixar == 's'.upper()):
				nome = input("Nome do arquivo.: ")
				print(download(self,nome))
		if options == "2":
			listar(self,'public_html')
			isdirectory = input("Escolher diretório?(S)im/(N)ão.: ")
			if (isdirectory == 's' or isdirectory == 's'.upper()):
				directory = input("Digite o diretório....:")
				if (len(directory)) > 0:
					limparTela()
					listar(self,directory)
				else:
					return
		if options == "3":
			listar(self,'public_html')
			isdirectory = input("Escolher diretório?(S)im/(N)ão.: ")
			# set_trace()
			if (isdirectory == 's' or isdirectory == 's'.upper()):
				directory = input("Digite o diretório....:")
				if (directory):
					limparTela()
					listar(self,directory)
			else:
				upload(self,"zap.txt")
				listar(self,'public_html')
		else:
			options = "5"
	return

def menu():
	limparTela()
	print(u"\nQual FTP conectar?\n")
	print("(1) FABRIZIO\n")
	print("(2) LUCIANO\n")
	print("(5) Sair do Script FTP\n")
	options = input("Escolha uma das opções acima..:")
	return ftps(options)

def main():
	options = ""
	while options != "5":
		options = menu()

main()
# json_string = json.dumps(config('LUCIANO'))
# json_string = json.loads(json_string)
# print(json_string["login"])
# os.environ['DEBUG'] = True
'''
login = "luxucom"
senha = "L3LCoMux@4BrL#"
arquivo = "ftp_via_python.txt"
'ftp.luxu.com.br'
login = "agenda"
senha = "W7@d4FF#S*"
host = '192.175.124.120'
arquivo = "test.php"

for a in os.environ:
	print('Var: ', a, 'Value: ', os.getenv(a))
if os.environ['PUBLIC']:
    print(True)
else:
    print(False)
    # main()
'''
# listar()
# upload()
# download()
