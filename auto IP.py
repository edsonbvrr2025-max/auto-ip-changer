# -*- coding: utf-8 -*-

import time
import os
import subprocess







try:

    import requests
except Exception:
    print('[+] O módulo requests do Python 3 não está instalado')
    os.system('solicitações de instalação do pip3')
    os.system('pip3 instalar solicitações[socks]')
    print('[!] O módulo requests do Python 3 está instalado ')
try:

    check_tor = subprocess.check_output('which tor', shell=True)
except subprocess.CalledProcessError:

    print('[+] O Tor não está instalado!')
    subprocess.check_output('sudo apt update',shell=True)
    subprocess.check_output('sudo apt install tor -y',shell=True)
    print('[!] O Tor foi instalado com sucesso ')

os.system("clear")
def ma_ip():
    url='http://checkip.amazonaws.com'
    get_ip= requests.get(url,proxies=dict(http='socks5://127.0.0.1:9050',https='socks5://127.0.0.1:9050'))
    return get_ip.text

def change():
    os.system("serviço tor recarregar")
    print ('[+] Seu endereço IP foi alterado para : '+str(ma_ip()))

print('''\033[1;32;40m \n
╔═══════════════════════════════════════════════════╗
║ ▄▄▄        █    ██ ▄▄▄█████▓ ▒█████      ██▓ ██▓███       ║
║▒████▄      ██  ▓██▒▓  ██▒ ▓▒▒██▒  ██▒   ▓██▒▓██░  ██▒   ║
║▒██  ▀█▄   ▓██  ▒██░▒ ▓██░ ▒░▒██░  ██▒   ▒██▒▓██░ ██▓▒  ║
║░██▄▄▄▄██  ▓▓█  ░██░░ ▓██▓ ░ ▒██   ██░   ░██░▒██▄█▓▒ ▒ 	║
║ ▓█   ▓██▒ ▒▒█████▓   ▒██▒ ░ ░ ████▓▒░   ░██░▒██▒ ░  ░ 	║
║ ▒▒   ▓▒█░ ░▒▓▒ ▒ ▒   ▒ ░░   ░ ▒░▒░▒░    ░▓  ▒▓▒░ ░  ░    	║
║  ▒   ▒▒ ░ ░░▒░ ░ ░     ░      ░ ▒ ▒░     ▒ ░░▒ ░             	║
║  ░   ▒     ░░░ ░ ░   ░      ░ ░ ░ ▒      ▒ ░░░               	║
║      ░  ░    ░                  ░ ░      ░                   		║
║                                                              			║
║        		>>> INITIALIZING AUTO IP SYSTEM v2.2 <<<              	║
║                                                              			║
║                           											║
║                                										║
║        			[✓] Assigning automatic IP...                 		║
║                                   									║
║                                                              			║
║                 		>> AUTO IP ONLINE <<                         	║
╚═══════════════════════════════════════════════════╝
from mrFD
''')
print("\033[1;40;31m http://facebook.com/ninja.hackerz.kurdish/\n")

os.system("service tor start")




time.sleep(3)
print("\033[1;32;40m change your  SOCKES to 127.0.0.1:9050 \n")
os.system("serviço para iniciar")
x = input("[+] Tempo para alterar o IP em segundos [type=60] >> ")
lin = input("[+] Quantas vezes você deseja alterar seu IP? Digite para alterar seu IP infinitamente] >> ") or "0"

try:
    lin = int(lin)

    if lin == 0:
        print("Iniciando troca infinita de IP. Pressione Ctrl+C para parar.")
        while True:
            try:
                time.sleep(int(x))  # Assuming 'x' is defined earlier in your code
                change()  # Assuming 'change()' is defined elsewhere
            except KeyboardInterrupt:
                print('\nAuto IP changer is closed.')
                break
    else:
        for _ in range(lin):
            time.sleep(int(x))  # Assuming 'x' is defined earlier in your code
            change()  # Assuming 'change()' is defined elsewhere

except ValueError:
    print("Entrada inválida. Por favor, insira um número válido.")
