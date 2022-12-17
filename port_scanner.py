import socket 
import os
import threading
from datetime import datetime
import colorama 
from colorama import Fore
import pyfiglet

#style du titre
title=pyfiglet.figlet_format("PORT_SCANNER")
print(title)


target = input('Entrez hôte cible: ')


print('-'*50)
print('scanning: ' + target)
print('Time started: ' + str(datetime.now()))
print('-'*50)

Ports= []

def scan(port):
        
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        try:
                s.connect((target,port))
                s.close()
                print(f'{Fore.CYAN} port {Fore.RED}[{port}] {Fore.CYAN} est ouvert')
                Ports.append(port)
        except:
                 print(f'{Fore.CYAN} port {Fore.RED}[{port}] {Fore.GREEN} est fermé', end='\r')       
                


scanned=1
for port in range(1, 2500):
        thread=threading.Thread(target=scan, kwargs={'port': scanned})
        scanned += 1
        thread.start()
print(f'{scanned} les ports ont été scannés')
print('Ports Ouverts: '+str(Ports))