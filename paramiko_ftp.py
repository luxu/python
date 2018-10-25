import paramiko
import configparser

# Carrega as configurações de arquivo externo
config = configparser.ConfigParser()
config.read('config.ini')

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect( hostname= "ftp.luxu.com.br", username="luxucom", password=config['luciano']['senha'])
stdin, stdout, stderr = ssh.exec_command("whoami")
print(stdout.read())
ssh.close()
