import os
choice = input('[+] Para instalar, pressione (Y). Para desinstalar, pressione (N) >> ')
run = os.system
if str(choice) =='Y' or str(choice)=='y':

    run('chmod 777 autoTOR.py')
    run('mkdir /usr/share/aut')
    run('cp autoTOR.py /usr/share/aut/autoTOR.py')

    cmnd=(' #! /bin/sh \n exec python3 /usr/share/aut/autoTOR.py "$@"')
    with open('/usr/bin/aut','w')as file:
        file.write(cmnd)
    run('chmod +x /usr/bin/aut & chmod +x /usr/share/aut/autoTOR.py')
    print('''\n\nParabéns, o Auto IP Changer foi instalado com sucesso! A partir de agora, basta digitar \x1b[6;30;42maut\x1b[0m in terminal ''')
if str(choice)=='N' or str(choice)=='n':
    run('rm -r /usr/share/aut ')
    run('rm /usr/bin/aut ')
    print('[!] O Auto Tor Ip changer foi removido com sucesso')
