import socket # for connecting
from colorama import init, Fore
import pyfiglet

#style du titre
title=pyfiglet.figlet_format("PORT_SCANNER")
print(title)
#Couleurs a patir de colorama
init()
CYAN = Fore.CYAN
RESET = Fore.RESET
RED = Fore.LIGHTRED_EX

def open_port(host, port):
    s = socket.socket()
    try:
        # tries to connect to host using that port
        s.connect((host, port))
        # make timeout if you want it a little faster ( less accuracy )
        s.settimeout(0.2)
    except:
        # cannot connect, port is closed return false
        return False
    else:
        # the connection was established, port is open!
        return True

# get the host from the user
host = input("Enter the host:")
# iterate over ports, from 1 to 1024
for port in range(1, 1025):
    if open_port(host, port):
        print(f"{CYAN}[+] {host}:{port} is open      {RESET}")
    else:
        print(f"{RED}[!] {host}:{port} is closed    {RESET}", end="\r")