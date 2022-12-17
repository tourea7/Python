import scapy.all as scapy
import argparse
import pyfiglet

#style du titre
title=pyfiglet.figlet_format("NETWORK_SCANNER")
print(title)


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Spécifiez l'adresse IP cible ou la plage d'adresses IP")
    options = parser.parse_args()
    return  options

def scan(ip):
        arp_packet = scapy.ARP(pdst=ip)
        broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_broadcast_packet = broadcast_packet/arp_packet
        answered_list = scapy.srp(arp_broadcast_packet, timeout=1, verbose=False)[0]
        client_list= []
        
        for element in answered_list:
                client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
                client_list.append(client_dict)
                
        return client_list

def print_result(scan_list):
        print("Ip\t\t\tMac\n------------------------------- ")
        for client in scan_list:
                print(client["ip"]+ "\t\t" + client["mac"])
        

options = get_arguments()
result_list = scan(options.target)
print_result(result_list)