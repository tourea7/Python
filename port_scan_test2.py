import argparse
import socket # for connecting
from colorama import init, Fore
from threading import Thread, Lock
from queue import Queue
import pyfiglet

#style du titre
title=pyfiglet.figlet_format("PORT_SCANNER")
print(title)
#Couleurs a patir de colorama
init()
CYAN = Fore.CYAN
RESET = Fore.RESET
RED = Fore.LIGHTRED_EX
# number of threads
N_THREADS = 200
# thread queue
q = Queue()
print_lock = Lock()


        
def port_scan(port):
    try:
        s = socket.socket()
        s.connect((host, port))
    except:
        with print_lock:
            print(f"{RED}{host:15}:{port:5} is closed  {RESET}", end='\r')
    else:
        with print_lock:
            print(f"{CYAN}{host:15}:{port:5} is open    {RESET}")
    finally:
        s.close()
              
def scan_thread():
    global q
    while True:
        # get the port number from the queue
        worker = q.get()
        # scan that port number
        port_scan(worker)
        # tells the queue that the scanning for that port 
        # is done
        q.task_done()
        
def main(host, ports):  
    host  
    global q
    
    for t in range(N_THREADS):
        # for each thread, start it
        t = Thread(target=scan_thread)
        # when we set daemon to true, that thread will end when the main thread ends
        t.daemon = True
        # start the daemon thread
        t.start()
    for worker in ports:
        # for each port, put that port into the queue
        # to start scanning
        q.put(worker)
    # wait the threads ( port scanners ) to finish
    q.join()

if __name__ == "__main__":
    host = input("Enter the host:")
    # parse some parameters passed
    parser = argparse.ArgumentParser(description="Simple port scanner")
    parser.add_argument("host", help="Host to scan.")
    parser.add_argument("--ports", "-p", dest="port_range", default="1-65535", help="Port range to scan, default is 1-65535 (all ports)")
    args = parser.parse_args()
    host, port_range = args.host, args.port_range

    start_port, end_port = port_range.split("-")
    start_port, end_port = int(start_port), int(end_port)

    ports = [ p for p in range(start_port, end_port)]

    main(host, ports)
