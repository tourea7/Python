import socket #module pour le reseau

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET crée un TCP et SOCK_STREAM crée UDP
serveur.bind(("192.168.1.2",5000))  #pour rendre sa machine serveur avec l'adresse ip
serveur.listen(5)  #precise le nombre de machines pouvant se connecter
print("Serveur en ecoute !")
while True:
    client,infoclient = serveur.accept()  #accepter les clients
    print('Connexion établie avec', infoclient[0])
    requete = client.recv(255).decode('utf-8') # ce que renvoi le client sous forme d'octet
    print('Yasmine:',requete)  #afficher la requete après decodage
    reponse = input('Vous: ')
    client.send(reponse.encode("utf-8"))  #envoyer un message au client sous forme encodé
    client.close()
    serveur.close()